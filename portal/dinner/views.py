# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db.models.functions import datetime
from django.shortcuts import render
from django.contrib import auth

from dinner.models import Food, Menu
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from workWithDate import Date
import json as simplejson
from django.http import HttpResponse
import json


def get_user(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render(request, 'dinner/base.html', {"user": username})



def login(request):
    return render(request, 'dinner/login.html', {})

def basket(request):
    return render(request, 'dinner/basket.html', {})


def loginSys(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        inputUser = request.POST.get('inputUser', '')
        print inputUser
        inputPassword = request.POST.get('inputPassword', '')
        user = auth.authenticate(username=inputUser, password = inputPassword)
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
    year = enterDate[0]
    month = enterDate[1]
    day = enterDate[2]
    # a = datetime.date(day, month, year)
    # print a.isoweekday()
    # datee = datetime.date(year=year,month=month,day=day)
    # print  datee.isoweekday()

    datas = {
        "foods": food,
        "menu": menu,
        "date": foodDay,

    }
    return render(request,'dinner/dinnerMenu.html', datas)

def home(request):
    return render(request, 'dinner/home.html', {})

def getPrice(request):
    first = request.GET.get('first','')
    garnir = request.GET.get('garnir','')
    salat = request.GET.get('salat','')
    miasne =  request.GET.get('miasne','')
    fruits =  request.GET.get('fruits','')
    complex =  request.GET.get('complex','')

    count = 0

    if (first != "" and garnir!="" and salat!="" and miasne!=""):       #1+2(гарнір+м"ясне)+салат
        count = count + 45
    elif(first == "" and garnir!="" and salat!="" and miasne!=""):      #2(гарнір+м"ясне)+салат
        count = count+39
    elif (first != "" and garnir != "" and salat == "" and miasne != ""): #1+2(гарнір+м"ясне)
        count = count + 39
    elif (first != "" and garnir == "" and salat != "" and miasne != ""):
        count = count + 39
    elif (first != "" and garnir == "" and salat == "" and miasne == ""):  #only first
        count = count + 12
    elif (first == "" and garnir != "" and salat == "" and miasne == ""):   # only garnir
        count = count + 12
    elif (first == "" and garnir == "" and salat == "" and miasne != ""): # miasne
        count = count + 27
    elif (first == "" and garnir == "" and salat != "" and miasne == ""): #salat
        count = count + 12
    elif (first != "" and garnir != "" and salat == "" and miasne == ""):  # перше + гарнір
        count = count + 24
    elif (first != "" and garnir != "" and salat != "" and miasne == ""):  # перше + гарнір + салат
        count = count + 36
    elif (first != "" and garnir == "" and salat != "" and miasne == ""):  # перше + салат
        count = count + 24
    if (fruits!=""):
        count = count+16
    if (complex!=""):
        count = count+33
    res ={'price': count}
    return HttpResponse(json.dumps(res), content_type='application/json')