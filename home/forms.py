from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Search',max_length=150)

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label='User name :')
    email = forms.EmailField(max_length=200,label='Email :')
    first_name = forms.CharField(max_length=100,label='First name :', help_text='First name')
    last_name = forms.CharField(max_length=100,label='Last name :',help_text='Last name')


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2',)