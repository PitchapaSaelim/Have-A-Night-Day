from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'sleep_time_management/home.html')

@login_required
def information(request):
    return render(request, 'sleep_time_management/information.html')

@login_required
def mainprofile(request):
    return render(request, 'sleep_time_management/mainprofile.html')

@login_required
def editprofile(request):
    return render(request, 'sleep_time_management/editprofile.html')

@login_required
def calculator2(request):
    return render(request, 'sleep_time_management/calculator2.html')

@login_required
def calculator3(request):
    return render(request, 'sleep_time_management/calculator3.html')

@login_required
def logout_view(request):
    logout(request)
    
    return redirect("/login")
