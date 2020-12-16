"""Model for sleep time management that contains the essential fields and behaviors of the data."""
from django.db import models
from django.contrib.auth.models import User


class Eventtime(models.Model):
    """Class contains the essential fields and store database."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wake_time = models.IntegerField(default=0, help_text='wake time')
    bed_time = models.IntegerField(default=0, help_text='bedtime')
    bed_event_time = models.IntegerField(default=0, help_text='bed event time')
    wake_event_time = models.IntegerField(
        default=0, help_text='wake event time')
    sleep_data = models.TextField(default='', help_text='sleep data')
    date = models.DateTimeField('date eventtime', null=True) 

    def __str__(self):
        """Return the username."""
        return self.user.username

    def calculate_sleep_wake_data(self):
        """Sleep data from calculating the wake-up time."""
        sleep_data = calculate_sleep_wake(self.wake_time, self.bed_event_time)
        return sleep_data

    def calculate_sleep_bed_data(self):
        """Sleep data from calculating the sleep time."""
        sleep_data = calculate_sleep_bed(self.bed_time, self.wake_event_time)
        return sleep_data


def calculate_sleep_wake(waketime, bed_event_time):
    """Calculate sleep data by using wake-up time."""
    if waketime < bed_event_time:
        waketime += 24*60
    get_wake_data = waketime - bed_event_time
    get_hr_wake_data = get_wake_data//60
    get_min_wake_data = get_wake_data % 60
    sleep_data = f"{get_hr_wake_data}.{get_min_wake_data} hours"
    return sleep_data


def calculate_sleep_bed(bedtime, wake_event_time):
    """Calculate sleep data by using bed time."""
    if wake_event_time < bedtime:
        wake_event_time += 24*60
    get_bed_data = wake_event_time - bedtime
    get_hr_bed_data = get_bed_data//60
    get_min_bed_data = get_bed_data % 60
    sleep_data = f"{get_hr_bed_data}.{get_min_bed_data} hours"
    return sleep_data
