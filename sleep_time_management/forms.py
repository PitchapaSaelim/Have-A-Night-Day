"""Form for sleep time management which is describes the logical structure of an object, its behavior, and the way its parts are represented to us."""
from django import forms

from django.contrib.auth.models import User
from datetime import date
from user.models import Profile


class UserUpdateForm(forms.ModelForm):
    """Class to update about user information."""

    class Meta:
        """Class that container with some options (metadata) attached to the model."""

        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    """Class to update about user's profile."""

    class Meta:
        """Class that container with some options (metadata) attached to the model."""

        model = Profile
        fields = ['birth_date', 'gender'] 

    def clean(self):
        """Check format about gender and birth date."""
        cleaned_data = super(ProfileUpdateForm, self).clean()
        dob = cleaned_data.get("birth_date")
        input_gender = cleaned_data.get("gender")
        today = date.today()
        if input_gender != "Male" and input_gender != "Female":
            raise forms.ValidationError("Please input only Male or Female")
        if dob.year > today.year:
            raise forms.ValidationError("Please input a valid birth date!")
        return cleaned_data
