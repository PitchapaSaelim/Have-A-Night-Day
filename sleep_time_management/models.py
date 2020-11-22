from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Eventtime(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wake_time = models.IntegerField(default=0, help_text='wake time')
    bed_time = models.IntegerField(default=0, help_text='bedtime')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timeevents')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_eventtime(sender, instance, created, **kwargs):
    if created:
        Eventtime.objects.create(user=instance)
    instance.eventtime.save()
