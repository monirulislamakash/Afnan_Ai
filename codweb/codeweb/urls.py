from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('skill',views.skill,name="skill"),
    path('contact',views.contact,name="contact"),
    path(r'^error',views.error,name="error"),
    path(r'^error1',views.error500,name="error500")
]