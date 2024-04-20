from django.forms import ModelForm
from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm, \
AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Create_blog_form(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
              "title": forms.TextInput(attrs={"class":"form-control", "style": "width: 300px;"}),
            "author": forms.TextInput(attrs={"class":"form-control", "style": "width: 300px;"}),
            "tags": forms.TextInput(attrs={"class":"form-control", "style": "width: 300px;"}),
            "category": forms.Select(attrs={"class": "form-control", "style": "width: 300px;"}),
        }




class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.
                PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.
                PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'User Name', 'first_name': 'First Name', 
                'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
            }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"), strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )