# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import os
from rexec import FileWrapper
from xml.dom.minidom import Document

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


def debtors(request):
     today = datetime.date.today()
     newdate = today.isoformat()
     orders = FoodsCustom.objects.filter(paymentFood="")
     return render(request, 'manager/homeManager.html', {'orders': orders, 'today': newdate})

def downloadzvit(request):
     a = request.GET.get('FoodsCustom')

     print type(a)
     print "sdsdsdsdsdsds"



     today = datetime.date.today()
     orders = FoodsCustom.objects.filter(dinnerDate=today)


     book = xlwt.Workbook('utf8')
     font = xlwt.easyxf('font: height 240,name Arial,colour_index black, bold off,\
             italic off; align: wrap on, vert top, horiz left;\
             pattern: pattern solid, fore_colour green;')
     sheet = book.add_sheet('sheetname')
     sheet.write(0, 0, 'Username', font)
     sheet.write(0, 1, 'Ім"я', font)
     sheet.write(0, 2, 'Прізвище', font)
     sheet.write(0, 3, 'Перше', font)
     sheet.write(0, 4, 'Гарнір', font)
     sheet.write(0, 5, 'Салат', font)
     sheet.write(0, 6, 'М"ясне', font)
     sheet.write(0, 7, 'Фрукти', font)
     sheet.write(0, 8, 'Комплексне', font)
     sheet.write(0, 9, 'Дата замовлення', font)
     sheet.write(0, 10, 'Дата доставки', font)
     sheet.write(0, 11, 'Сума (грн)', font)
     sheet.write(0, 12, 'Оплата', font)
     sheet.row(0).height = 800
     sheet.col(0).width = 4000
     sheet.col(1).width = 4000
     sheet.col(2).width = 4000
     sheet.col(3).width = 4000
     sheet.col(4).width = 4000
     sheet.col(5).width = 4000
     sheet.col(6).width = 4000
     sheet.col(7).width = 4000
     sheet.col(8).width = 4000
     sheet.col(9).width = 4000
     sheet.col(10).width = 4000
     sheet.col(11).width = 4000
     sheet.col(12).width = 4000
     i=0
     for data in orders:
          i = i+1
          sheet.write(i, 0, data.customUserName )
          sheet.write(i, 1, data.customFirstName)
          sheet.write(i, 2, data.customLastName)
          sheet.write(i, 3, data.firstFood )
          sheet.write(i, 4, data.garnish )
          sheet.write(i, 5, data.salad)
          sheet.write(i, 6, data.meatDish)
          sheet.write(i, 7, data.fruits)
          sheet.write(i, 8, data.complex)
          sheet.write(i, 9, data.customDate)
          sheet.write(i, 10, data.dinnerDate)
          sheet.write(i, 11, data.customPrice)
          sheet.write(i, 12, data.paymentFood)



     sheet.portrait = False
     sheet.set_print_scaling(85)
     name = today.isoformat()
     book.save(name+'.xls')


     filename = name+'.xls'
     content_type = 'application/vnd.ms-excel'
     file_path = os.path.join("../portal/", filename)
     response = HttpResponse(FileWrapper(file(file_path)), content_type=content_type)
     response['Content-Disposition'] = 'attachment; filename=%s' % (
          filename.encode('utf-8') if isinstance(filename, unicode) else filename,
     )
     # response['Content-Length'] = os.path.getsize('/')
     return response
     # return HttpResponse(json.dumps(response), content_type='application/json')