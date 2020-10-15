from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sleep_time_management/home.html')

def information(request):
    return render(request, 'sleep_time_management/information.html')