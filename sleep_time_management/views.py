from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import UserUpdateForm, ProfileUpdateForm

from .models import Eventtime

from django.http import JsonResponse

from django.utils import timezone
from datetime import date
from django.contrib import messages


def get_age_span(age):
    if 1 >= age or age <= 2:
        return 'Toddler'
    elif 3 >= age or age <= 5:
        return 'Preschool'
    elif 6 >= age or age <= 13:
        return 'School age'
    elif 14 >= age or age <= 17:
        return 'Teenager'
    elif 18 >= age or age <= 25:
        return 'Young adult'
    elif 26 >= age or age <= 64:
        return 'Adult'
    elif age >= 65:
        return 'Older adult'


def get_sleep_hour(age_span):
    if age_span == 'Toddler':
        return '11-14 hours'
    elif age_span == 'Preschool':
        return '10-13 hours'
    elif age_span == 'School age':
        return '9-11 hours'
    elif age_span == 'Teenager':
        return '8-10 hours'
    elif age_span == 'Young adult':
        return '7-9 hours'
    elif age_span == 'Adult':
        return '7-9 hours'
    elif age_span == 'Older adult':
        return '7-8 hours'


def get_disease_list(age, gender, average_sleep):
    disease = []
    hour = float(average_sleep)
    if 25 >= age or age <= 59:
        if hour <= 5:
            disease.append("Hypertension")
    elif 60 >= age or age <= 86:
        if hour >= 9:
            disease.append("Hypertension")
    if hour > 10:
        disease.append("Breast cancer risk")
    if gender == "Female":
        if age < 60:
            if hour < 6:
                disease.append("Coronary heart disease (CHD)")
        if age > 65:
            if hour < 5 or hour > 9:
                disease.append("Depression")
        if hour > 9:
            disease.append("Infertility")
    elif gender == "Male":
        if 40 >= age or age <= 79:
            if hour < 5:
                disease.append("Coronary heart disease (CHD)")
        if age > 50:
            disease.append("REM Sleep Disorder")
        if 40 >= age or age <= 70:
            if hour != 7:
                disease.append(
                    "Diabetes mellitus (DM) /Impaired glucose tolerance (IGT)")
        elif 53 >= age or age <= 93:
            if hour != 7 or hour != 8:
                disease.append(
                    "Diabetes mellitus (DM) /Impaired glucose tolerance (IGT)")
    if 18 >= age or age <= 35:
        if hour < 6:
            disease.append("Stroke")
    elif 35 >= age or age <= 45:
        if hour < 6:
            disease.append("Stroke")
    elif 46 >= age or age <= 55:
        if hour < 6:
            disease.append("Stroke")
    elif 55 >= age or age <= 65:
        if hour < 6:
            disease.append("Stroke")
    elif 65 >= age or age <= 80:
        if hour > 8:
            disease.append("Stroke")
    if hour < 6:
        disease.append("Colorectal cancer")
    if hour > 8:
        disease.append("Hypersomnia")
    return disease


@login_required
def home(request):
    return render(request, 'sleep_time_management/home.html')


def information(request):
    return render(request, 'sleep_time_management/information.html')


@login_required
def mainprofile(request):
    disease_list = []
    today = date.today()
    birthday = request.user.profile.birth_date
    age = today.year - birthday.year - \
        ((today.month, today.day) < (birthday.month, birthday.day))
    age_span = get_age_span(age)
    request.user.profile.age_span = age_span
    average = request.user.profile.calculate_average()
    request.user.profile.average = average
    request.user.profile.save()
    disease_list = get_disease_list(age, request.user.profile.gender, average)
    return render(request, 'sleep_time_management/mainprofile.html', {'age': age, 'disease_list': disease_list})


@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return render(request, 'sleep_time_management/mainprofile.html')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'sleep_time_management/editprofile.html', context)


@login_required
def calculator2(request):
    return render(request, 'sleep_time_management/calculator2.html')


@login_required
def calculator3(request):
    return render(request, 'sleep_time_management/calculator3.html')


@login_required
def about_us(request):
    return render(request, 'sleep_time_management/aboutus.html')


@login_required
def contact_us(request):
    return render(request, 'sleep_time_management/contactus.html')


@login_required
def logout_view(request):
    logout(request)

    return redirect("/login")


def calculate2_view(request):
    if request.method == 'POST':
        sleep_hour = get_sleep_hour(request.user.profile.age_span)
        waketime = request.POST["waketime"]
        if waketime != "":
            time = waketime.split(':')
            caltime = (int(time[0])*60)+int(time[1])
            today = date.today()
            if Eventtime.objects.filter(user=request.user, date__day=today.day).exists():
                wake_time = Eventtime.objects.filter(
                    user=request.user, date__day=today.day).first()
            else:
                wake_time = Eventtime.objects.create(
                    user=request.user, date=timezone.now())
            wake_time.wake_time = caltime
            wake_time.save()
            listtime = calculate_waketime(waketime=waketime)
            return render(request, 'sleep_time_management/calculator2.html', {'waketime': listtime, 'sleep_hour': sleep_hour})
        else:
            messages.warning(request, "Please input AM or PM")
            return render(request, 'sleep_time_management/home.html')


def calculate_waketime(waketime):
    time = waketime.split(':')
    caltime = (int(time[0])*60)+int(time[1])
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
    return listtime


def calculate_sleeptime(sleeptime):
    time = sleeptime.split(':')
    caltime = (int(time[0])*60)+int(time[1])
    listtime = []
    for i in range(6):
        caltime += 90
        hour = caltime//60
        minute = caltime % 60
        if (hour == 24):
            hour = '00'
        if (minute == 0):
            minute = '00'
        elif (int(minute) < 10):
            minute = str(minute)
            minute = '0'+minute
        if(int(hour) > 24):
            hour = hour - 24
        listtime.append(f"{hour}:{minute}")
    return listtime


def calculate3_view(request):
    if request.method == 'POST':
        sleep_hour = get_sleep_hour(request.user.profile.age_span)
        sleeptime = request.POST["sleeptime"]
        if sleeptime != "":
            time = sleeptime.split(':')
            caltime = (int(time[0])*60)+int(time[1])
            today = date.today()
            bed_time = Eventtime.objects.filter(
                user=request.user, date__day=today.day).first()
            bed_time.bed_time = caltime
            bed_time.save()
            listtime = calculate_sleeptime(sleeptime=sleeptime)
            return render(request, 'sleep_time_management/calculator3.html', {'sleeptime': listtime, 'sleep_hour': sleep_hour})
        else:
            messages.warning(request, "Please input AM or PM")
            return render(request, 'sleep_time_management/home.html')


def bed_sleep_data(request):
    if request.method == 'POST':
        get_bed_event_time = request.POST["bed_event_time"]
        time = get_bed_event_time.split(':')
        cal_bed_time = (int(time[0])*60)+int(time[1])
        today = date.today()
        bed_event_time = Eventtime.objects.filter(
            user=request.user, date__day=today.day).first()
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


def sleep_chart(request):
    labels = []
    data = []
    count = 1

    queryset = Eventtime.objects.filter(user=request.user).values('sleep_data')

    for i in queryset:
        time = i['sleep_data'].split(" ")
        date = "Day " + str(count)
        labels.append(date)
        data.append(float(time[0]))
        count += 1

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
