from django.db import models


class User(models.Model):
    GENDER_MALE = 0         
    GENDER_FEMALE = 1 
    GENDER_NOT_SPECIFIED = 2
    GENDER_OTHERS = 3        
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), 
                      (GENDER_FEMALE, 'Female'),
                      (GENDER_NOT_SPECIFIED, 'Not Specified'),
                      (GENDER_OTHERS, 'Others')] 

    gender = models.IntegerField(choices=GENDER_CHOICES)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateTimeField('birthdate')
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name  

    # profile_image = ImageField(upload_to='media', blank=True, null=True)

class EventTime(models.Model): 
    wake_time = models.DateTimeField('wake time')
    bed_time = models.DateTimeField('bedtime')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timeevents')
