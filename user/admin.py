"""Used to display the models in the Django admin panel."""
from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
