# Generated by Django 3.1 on 2020-11-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_time_management', '0006_eventtime_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtime',
            name='event_time',
        ),
        migrations.AddField(
            model_name='eventtime',
            name='bed_event_time',
            field=models.IntegerField(default=0, help_text='bed event time'),
        ),
    ]