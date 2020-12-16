from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
from datetime import date


class NewForm(UserCreationForm):
    fname = forms.CharField(label='First name', max_length=100)
    lname = forms.CharField(label='Last name', max_length=100)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    gender = forms.CharField(
        label='Gender', max_length=10, help_text='Required. Female or Male')

    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'email',
                  'birth_date', 'gender', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(NewForm, self).clean()
        dob = cleaned_data.get("birth_date")
        input_gender = cleaned_data.get("gender")
        today = date.today()
        if input_gender != "Male" and input_gender != "Female":
            raise forms.ValidationError("Please input only male or female")
        if dob.year > today.year:
            raise forms.ValidationError("Please input a valid birth date!")
        return cleaned_data

    def save(self, commit=True):
        user = super(NewForm, self).save(commit=False)
        user.first_name = self.cleaned_data["fname"]
        user.last_name = self.cleaned_data["lname"]
        if commit:
            user.save()
        return user
        