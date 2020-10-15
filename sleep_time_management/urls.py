from django.contrib import admin
from django.urls import path
from . import views

app_name = 'sleep_time_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('information/', views.information, name='information')
]
