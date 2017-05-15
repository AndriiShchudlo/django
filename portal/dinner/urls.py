from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', views.login, name="login"),
    url(r'^$', views.home, name="home"),
    url(r'^menu/', views.dinnerMenu, name="dinnerMenu"),
    url(r'^orders/', views.reviewOrders, name="reviewOrders"),
    url(r'^loginSys/', views.loginSys, name="loginSys"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^get_price/', views.getPrice, name="getPrice"),
    url(r'^addDinner/', views.addDinner, name="addDinner"),
]
