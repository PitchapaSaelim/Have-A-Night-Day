from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Eventtime(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wake_time = models.IntegerField(default=0, help_text='wake time')
    bed_time = models.IntegerField(default=0, help_text='bedtime')
    bed_event_time = models.IntegerField(default=0, help_text='bed event time')
    wake_event_time = models.IntegerField(
        default=0, help_text='wake event time')
    sleep_data = models.TextField(default='', help_text='sleep data')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timeevents')

    def __str__(self):
        return self.user.username

    def calculate_sleep_wake_data(self):
        if self.wake_time < self.bed_event_time:
            self.wake_time += 24*60
        get_wake_data = self.wake_time - self.bed_event_time
        get_hr_wake_data = get_wake_data//60
        get_min_wake_data = get_wake_data % 60
        sleep_data = f"{get_hr_wake_data}.{get_min_wake_data} hours"
        return sleep_data

    def calculate_sleep_bed_data(self):
        if self.wake_event_time < self.bed_time:
            self.wake_event_time += 24*60
        get_bed_data = self.wake_event_time - self.bed_time
        get_hr_bed_data = get_bed_data//60
        get_min_bed_data = get_bed_data % 60
        sleep_data = f"{get_hr_bed_data}.{get_min_bed_data} hours"
        return sleep_data


@receiver(post_save, sender=User)
def update_user_eventtime(sender, instance, created, **kwargs):
    if created:
        Eventtime.objects.create(user=instance)
    instance.eventtime.save()
