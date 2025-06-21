from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser, Profile


class RegisterForm(UserCreationForm):
    class Meta:
        fields = ['email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'image', 'bio', 'phone']