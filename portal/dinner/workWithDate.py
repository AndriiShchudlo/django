import datetime


class Date:
    def getFoodFromDay(request):

        foodDay = request.get('dinnerDate', '')
        print foodDay



date = datetime.date(day=21, month=12, year=2016)
print  date.isoweekday()