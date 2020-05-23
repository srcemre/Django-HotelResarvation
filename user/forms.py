from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'table', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'table', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'table', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'table', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Karaman', 'Karaman'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'table', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'table', 'placeholder': 'address'}),
            'city': TextInput(attrs={'class': 'table', 'placeholder': 'city'}),
            'country': TextInput(attrs={'class': 'table', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'aa-secondary-btn', 'placeholder': 'image'}),
        }
