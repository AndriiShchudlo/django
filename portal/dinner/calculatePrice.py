# -*- coding: utf-8 -*-
class CalculatePrice(object):
    COMPLEX1 = 45    # 1+2(гарнір+м"ясне)+салат
    COMPLEX2 = 39    # 2(гарнір+м"ясне)+салат
    COMPLEX3 = 39    # 1+2(гарнір+м"ясне)
    COMPLEX4 = 39    # 1+2(м"ясне) + салат
    FIRST_COURSE = 12  # Тільки перша страва
    GARNISH = 12       # тільки гарнір
    SALAD = 12         # сАЛАТ
    MEAT_DISH = 27      # Тільки м'ясне
    FRUITS = 16
    COMPLEX = 33    # Вареники, деруни, млинці ...

    def getPrice(self, request):
        calculate = CalculatePrice()
        first = request.GET.get('first', '')
        garnir = request.GET.get('garnir', '')
        salat = request.GET.get('salat', '')
        miasne = request.GET.get('miasne', '')
        fruits = request.GET.get('fruits', '')
        complex = request.GET.get('complex', '')
        count = 0
        if (first != "" and garnir != "" and salat != "" and miasne != ""):  # 1+2(гарнір+м"ясне)+салат
            count = count + calculate.COMPLEX1
            first = ""
            garnir = ""
            salat = ""
            miasne = ""
        elif (garnir != "" and salat != "" and miasne != ""):  # 2(гарнір+м"ясне)+салат
            count = count + calculate.COMPLEX2
            garnir = ""
            salat = ""
            miasne = ""
        elif (first != "" and garnir != "" and miasne != ""):  # 1+2(гарнір+м"ясне)
            count = count + calculate.COMPLEX3
            first = ""
            garnir = ""
            miasne = ""
        elif (first != "" and salat != "" and miasne != ""):
            count = count + calculate.COMPLEX4
            first = ""
            salat = ""
            miasne = ""
        if (first != ""):  # only first
            count = count + calculate.FIRST_COURSE
            first = ""
        if (garnir != ""):  # only garnir
            count = count + calculate.GARNISH
            garnir = ""
        if (salat != ""):  # salat
            count = count + calculate.SALAD
            salat = ""
        if (miasne != ""):  # miasne
            count = count + calculate.MEAT_DISH
            miasne = ""
        if (fruits != ""):
            count = count + calculate.FRUITS
            fruits = ""
        if (complex != ""):
            count = count + calculate.COMPLEX
            complex = ""
        res = count
        return res