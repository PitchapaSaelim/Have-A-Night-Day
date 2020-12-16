from django import forms

from django.contrib.auth.models import User
from datetime import date
from user.models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date', 'gender']
    
    def clean(self):
        cleaned_data = super(ProfileUpdateForm, self).clean()
        dob = cleaned_data.get("birth_date")
        input_gender = cleaned_data.get("gender")
        today = date.today()
        if input_gender != "Male" and input_gender != "Female":
            raise forms.ValidationError("Please input only Male or Female")
        if dob.year > today.year:
            raise forms.ValidationError("Please input a valid birth date!")
        return cleaned_data
