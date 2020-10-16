"""Have_A_Night_Day URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from user.views import register_user_view
from user.views import login_view
from user.views import logout_view

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sleep_time_management.urls')),
    path('registeration/', register_user_view, name='register_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
