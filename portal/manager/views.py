# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from dinner.models import FoodsCustom
from django.shortcuts import render
from django.http import HttpResponse
import json
import xlwt
import urllib

def getControlPage(request):
    today = datetime.date.today()
    date = today.isoformat()
    orders = FoodsCustom.objects.filter(dinnerDate=today)
    return render(request, 'manager/homeManager.html', {'orders': orders, 'today':date})

def payDinner(request):
     print "aaaaaaaaaaaa"
     return HttpResponse(json.dumps("true"), content_type='application/json')

def filterDate(request):
     newDate = request.POST.get('newdate', '')
     orders = FoodsCustom.objects.filter(dinnerDate=newDate)
     return render(request, 'manager/homeManager.html', {'orders': orders, 'today': newDate})


def download(request):
     dataFromTable = request.GET.get('data','')

     today = datetime.date.today()
     orders = FoodsCustom.objects.filter(dinnerDate=today)

     for i in orders:
          customUserName = i.customUserName
          customFirstName = i.customFirstName
          customLastName = i.customLastName
          firstFood = i.firstFood
          garnish = i.garnish
          salad = i.salad
          meatDish = i.meatDish
          fruits = i.fruits
          complex = i.complex
          customDate = i.customDate
          dinnerDate = i.dinnerDate
          customPrice = i.customPrice
          paymentFood = i.paymentFood
     book = xlwt.Workbook('utf8')
     font = xlwt.easyxf('font: height 240,name Arial,colour_index black, bold off,\
         italic off; align: wrap on, vert top, horiz left;\
         pattern: pattern solid, fore_colour red;')
     sheet = book.add_sheet('sheetname')
     sheet.write(0, 0, 'text', font)
     sheet.row(1).height = 2500
     sheet.col(0).width = 20000
     sheet.portrait = False
     sheet.set_print_scaling(85)
     book.save('filename.xls')

     print book
     print dataFromTable
     return HttpResponse(json.dumps("true"), content_type='application/json')
