from django.contrib import admin
from django.urls import path

from . import views

app_name = 'sleep_time_management'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('mainprofile/', views.mainprofile, name='mainprofile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('calculator2/', views.calculator2, name='calculator2'),
    path('calculator3/', views.calculator2, name='calculator3'),

]
