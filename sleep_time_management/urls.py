from django.contrib import admin
from django.urls import path


from . import views

app_name = 'sleep_time_management'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('information/', views.information, name='information'),
    path('mainprofile/', views.mainprofile, name='mainprofile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('calculator2/', views.calculate2_view, name='calculator2'),
    path('calculator3/', views.calculate3_view, name='calculator3'),
    path('logout/', views.logout_view, name='logout'),
    path('bedeventtime/', views.bed_sleep_data, name='bed_sleep_data'),
    path('wakeeventtime/', views.wake_sleep_data, name='wake_sleep_data'),
    path('sleep-chart/', views.sleep_chart, name='sleep-chart')
]
