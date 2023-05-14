from django.contrib import admin
from django.urls import path
from User import views

urlpatterns = [
    path('', views.index , name="index"),
    path('login',views.userLogin,name="userLogin"),
    path('logout',views.userLogout,name="userLogout")
    
]