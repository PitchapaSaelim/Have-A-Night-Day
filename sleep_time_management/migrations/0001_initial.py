# Generated by Django 3.1 on 2020-10-16 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthdate', models.DateTimeField(verbose_name='birthdate')),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EventTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wake_time', models.IntegerField(default=0, help_text='bedtime')),
                ('bed_time', models.IntegerField(default=0, help_text='wake time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeevents', to='sleep_time_management.user')),
            ],
        ),
    ]