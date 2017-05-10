from django.conf.urls import url
from . import views

from . import views

urlpatterns = [
    url(r'^login/', views.login, name="login"),
    url(r'^$', views.home, name="home"),
    url(r'^menu/', views.dinnerMenu, name="dinnerMenu"),
    url(r'^basket/', views.basket, name="bascket"),
    url(r'^loginSys/', views.loginSys, name="loginSys"),
    url(r'^logout/', views.logout, name="logout"),

]
