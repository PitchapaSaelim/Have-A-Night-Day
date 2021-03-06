"""URLs path expressions for a web application."""
from django.urls import path

from . import views

app_name = 'sleep_time_management'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('mainprofile/information/', views.information, name='information'),
    path('mainprofile/', views.mainprofile, name='mainprofile'),
    path('mainprofile/edit', views.editprofile, name='editprofile'),
    path('calculator/waketime', views.calculate2_view, name='calculator2'),
    path('calculator/bed-time', views.calculate3_view, name='calculator3'),
    path('logout/', views.logout_view, name='logout'),
    path('calculator/bed-time/save', views.bed_sleep_data, name='bed_sleep_data'),
    path('calculator/waketime/save', views.wake_sleep_data, name='wake_sleep_data'),
    path('sleep-chart/', views.sleep_chart, name='sleep-chart'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us')
]
