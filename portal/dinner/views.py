# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
from django.shortcuts import render

from dinner.models import Food, Menu, CustomFood
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.http import HttpResponse
import json
from calculatePrice import CalculatePrice
from addDinner import AddDinner


def get_user(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'dinner/base.html', {"user": username})

def login(request):
    return render(request, 'dinner/login.html', {})


def loginSys(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        inputUser = request.POST.get('inputUser', '')
        print inputUser
        inputPassword = request.POST.get('inputPassword', '')
        user = auth.authenticate(username=inputUser, password=inputPassword)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Користувач не знайдений"
            return render_to_response('dinner/login.html', args)
    else:
        return render_to_response('dinner/login.html', args)

def logout(request):
     auth.logout(request)
     return redirect('/')

def dinnerMenu(request):
    food = Food.objects.all()
    menu = Menu.objects.all()
    foodDay = request.POST.get('dinnerDate', '')
    enterDate = foodDay.split("-")
    year = int(enterDate[0])
    month = int(enterDate[1])
    day = int(enterDate[2])
    openDateFood = datetime.date(year=year, month=month, day=day)
    openDateFood = openDateFood.isoweekday()
    datas = {
        "foods": food,
        "menu": menu,
        "date": foodDay,
        "openDateFood": openDateFood,

    }
    return render(request,'dinner/dinnerMenu.html', datas)

def home(request):
    return render(request, 'dinner/home.html', {})

def getPrice(request):
    newPrice = CalculatePrice()
    price = newPrice.getPrice(request)
    result = {'price': price}
    return HttpResponse(json.dumps(result), content_type='application/json')

def addDinner(request):
    dinner = AddDinner()
    res = dinner.addDinner(request)
    return HttpResponse(json.dumps(res), content_type='application/json')

def reviewOrders(request):
    username = request.user.username
    orders = CustomFood.objects.filter(customUserName=username)[:]
    return render(request, 'dinner/reviewOrders.html', {'orders': orders})
