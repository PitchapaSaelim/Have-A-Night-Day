"""Model for user that contains the essential fields and behaviors of the data."""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from sleep_time_management.models import Eventtime


class Profile(models.Model):
    """Class contains the essential fields and store database."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, default='')
    age_span = models.CharField(max_length=100, default='')
    average = models.CharField(max_length=100, default='', help_text='average sleep time')

    def calculate_average(self):
        """Calculate average of sleep data."""
        queryset = Eventtime.objects.filter(
            user=self.user).values('sleep_data')
        count = 0
        sums = 0
        for i in queryset:
            time = i['sleep_data'].split(" ")
            count += 1
            sums += float(time[0])
        if count == 0:
            return 0
        return sums/count

    def __str__(self):
        """Return the username."""
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """Update the user profile."""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save() 
