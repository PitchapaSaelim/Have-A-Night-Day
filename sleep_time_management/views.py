from django.shortcuts import render, redirect

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

def calculate2_view(request):
    if request.method == 'POST':
        waketime = request.POST["waketime"]
        time = waketime.split(':')
        caltime = (int(time[0])*60)+int(time[1])
        listtime = []
    
        for i in range(6):
            caltime -= 90
            if (caltime<0):
                caltime+=(24*60)
            hour = caltime//60
            minute = caltime%60
            if (int(minute)<10 and minute!=0) :
                minute = '0'+str(minute)
            if (minute==0) :
                minute = '00'
            listtime.append(f"{hour}:{minute}")
            if (hour <= 0):
                caltime += (24*60)
        return render(request,'sleep_time_management/calculator2.html',{'waketime': listtime})
        # return render(request,'sleep_time_management/calculator2.html',{'waketime': waketime})


def calculate3_view(request):
    if request.method == 'POST':
        sleeptime = request.POST["sleeptime"]
        time = sleeptime.split(':')
        caltime = (int(time[0])*60)+int(time[1])
        listtime = []
        for i in range(6):
            caltime += 90
            hour = caltime//60
            minute = caltime%60
            if (hour == 24):
                hour = '00'
            if (minute==0) :
                minute = '00'
            if(int(hour) > 24):
                hour= hour - 24
            listtime.append(f"{hour}:{minute}")
        return render(request,'sleep_time_management/calculator3.html',{'sleeptime': listtime})



