from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('skill',views.skill,name="skill"),
    path('contact',views.contact,name="contact"),
]