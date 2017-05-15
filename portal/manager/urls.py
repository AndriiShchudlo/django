from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^manager/', views.getControlPage, name="getControlPage"),
    url(r'^payDinner/', views.payDinner, name="payDinner"),
    url(r'^filterDate/', views.filterDate, name="filterDate"),
    url(r'^download/', views.download, name="download"),

]
