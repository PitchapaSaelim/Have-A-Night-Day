"""A View for application that show what you see when you render a website."""
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

from .form import NewForm


def register_user_view(request):
    """Render the registration page when the user created an account."""
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user.save()
            return redirect("sleep_time_management:home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="register.html",
                          context={"form": form})

    form = NewForm
    return render(request=request,
                  template_name="register.html",
                  context={"form": form})


def login_view(request):
    """Redirect to the home page when the user has logged in."""
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('sleep_time_management:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})


@login_required
def logout_view(request):
    """Redirect to the login page when the user has logged out."""
    logout(request)

    return redirect("/login")
