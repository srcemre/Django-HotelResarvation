from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    catid = forms.IntegerField()


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username :', max_length=30)
    email = forms.EmailField(label='Email :', max_length=100)
    first_name = forms.CharField(label='First Name :',help_text="Ahmet", max_length=100)
    last_name = forms.CharField(label='Last Name :',help_text="Yılmaz", max_length=100)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')
