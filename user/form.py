from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewForm(UserCreationForm):
    fname = forms.CharField(label='First name', max_length=100)
    lname = forms.CharField(label='Last name', max_length=100)

    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'password1', 'password2' ]

    def save(self, commit=True):
        user = super(NewForm, self).save(commit=False)
        user.first_name = self.cleaned_data["fname"]
        user.last_name = self.cleaned_data["lname"]
        if commit:
            user.save()
        return user