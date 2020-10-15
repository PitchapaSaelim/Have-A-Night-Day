from django.shortcuts import redirect

def index(request):
    return redirect('sleep_time_management:index')