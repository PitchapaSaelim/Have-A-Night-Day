from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import logout

def home(request):
    return render(request, 'sleep_time_management/home.html')

def information(request):
    return render(request, 'sleep_time_management/information.html')

def mainprofile(request):
    return render(request, 'sleep_time_management/mainprofile.html')

def editprofile(request):
    return render(request, 'sleep_time_management/editprofile.html')

def calculator2(request):
    return render(request, 'sleep_time_management/calculator2.html')

def calculator3(request):
    return render(request, 'sleep_time_management/calculator3.html')

def logout_view(request):
    logout(request)
    
    return redirect("/login")
