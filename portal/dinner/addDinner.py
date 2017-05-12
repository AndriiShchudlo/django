# -*- coding: utf-8 -*-
import datetime

from calculatePrice import CalculatePrice
from dinner.models import CustomFood


class AddDinner(object):
    def addDinner(self,request):
        newPrice = CalculatePrice()
        customUserName = request.user.username
        customFirstName = request.user.first_name
        customLastName = request.user.last_name
        firstFood = request.GET.get('first', '')
        garnish = request.GET.get('garnir', '')
        salad = request.GET.get('salat', '')
        meatDish = request.GET.get('miasne', '')
        fruits = request.GET.get('fruits', '')
        complex = request.GET.get('complex', '')
        customDate = datetime.date.today()
        dinnerDate = request.GET.get('dinnerDate', '')
        customPrice = newPrice.getPrice(request)

        customFood = CustomFood(
            customUserName=customUserName,
            customFirstName=customFirstName,
            customLastName=customLastName,
            firstFood=firstFood,
            garnish=garnish,
            salad=salad,
            meatDish=meatDish,
            fruits=fruits,
            complex=complex,
            customDate=customDate,
            dinnerDate=dinnerDate,
            customPrice=customPrice
        )
        customFood.save()
        return "True"