from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^manager/', views.getControlPage, name="getControlPage"),
    url(r'^payDinner/', views.payDinner, name="payDinner"),
    url(r'^filterDate/', views.filterDate, name="filterDate"),
    url(r'^debtors/', views.debtors, name="debtors"),
    url(r'^downloadzvit/', views.downloadzvit, name="downloadzvit"),

]
