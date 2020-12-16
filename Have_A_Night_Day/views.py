"""A View for application that show what you see when you render a website."""
from django.shortcuts import redirect


def index(request):
    """Redirect to the index page."""
    return redirect('sleep_time_management:index')
