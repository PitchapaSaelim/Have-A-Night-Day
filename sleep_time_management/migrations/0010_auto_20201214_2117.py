# Generated by Django 3.1 on 2020-12-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sleep_time_management', '0009_eventtime_sleep_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtime',
            name='bed_time',
            field=models.IntegerField(default=0, help_text='bedtime'),
        ),
        migrations.AlterField(
            model_name='eventtime',
            name='wake_time',
            field=models.IntegerField(default=0, help_text='wake time'),
        ),
    ]
