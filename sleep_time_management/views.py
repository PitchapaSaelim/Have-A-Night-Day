from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Eventtime


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
        wake_time = Eventtime.objects.filter(user=request.user).first()
        wake_time.wake_time = caltime
        wake_time.save()
        listtime = []
        for i in range(6):
            caltime -= 90
            if (caltime < 0):
                caltime += (24*60)
            hour = caltime//60
            minute = caltime % 60
            if (int(minute) < 10 and minute != 0):
                minute = '0'+str(minute)
            if (minute == 0):
                minute = '00'
            listtime.append(f"{hour}:{minute}")
            if (hour <= 0):
                caltime += (24*60)
        return render(request, 'sleep_time_management/calculator2.html', {'waketime': listtime})
        # return render(request,'sleep_time_management/calculator2.html',{'waketime': waketime})


def calculate3_view(request):
    if request.method == 'POST':
        sleeptime = request.POST["sleeptime"]
        time = sleeptime.split(':')
        caltime = (int(time[0])*60)+int(time[1])
        bed_time = Eventtime.objects.filter(user=request.user).first()
        bed_time.bed_time = caltime
        bed_time.save()
        listtime = []
        for i in range(6):
            caltime += 90
            hour = caltime//60
            minute = caltime % 60
            if (hour == 24):
                hour = '00'
            if (minute == 0):
                minute = '00'
            if(int(hour) > 24):
                hour = hour - 24
            listtime.append(f"{hour}:{minute}")
        return render(request, 'sleep_time_management/calculator3.html', {'sleeptime': listtime})


def bed_sleep_data(request):
    if request.method == 'POST':
        get_bed_event_time = request.POST["bed_event_time"]
        time = get_bed_event_time.split(':')
        cal_bed_time = (int(time[0])*60)+int(time[1])
        bed_event_time = Eventtime.objects.filter(user=request.user).first()
        bed_event_time.bed_event_time = cal_bed_time
        bed_event_time.save()
    bed_event_time.sleep_data = bed_event_time.calculate_sleep_wake_data()
    bed_event_time.save()
    return render(request, 'sleep_time_management/home.html')


def wake_sleep_data(request):
    if request.method == 'POST':
        get_wake_event_time = request.POST["wake_event_time"]
        time = get_wake_event_time.split(':')
        cal_wake_time = (int(time[0])*60)+int(time[1])
        wake_event_time = Eventtime.objects.filter(user=request.user).first()
        wake_event_time.wake_event_time = cal_wake_time
        wake_event_time.save()
    wake_event_time.sleep_data = wake_event_time.calculate_sleep_bed_data()
    wake_event_time.save()
    return render(request, 'sleep_time_management/home.html')
