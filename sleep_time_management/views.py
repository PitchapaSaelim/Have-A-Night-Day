from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'sleep_time_management/home.html')

def information(request):
    return render(request, 'sleep_time_management/information.html')

def mainprofile(request):
    return render(request, 'sleep_time_management/mainprofile.html')
