from django import forms
from django.forms import ModelForm
from .models import Player


class PlayerSigninForm(ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 70, 'rows': 7, 'placeholder': 'Write about yourself...'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username...'}))
    email_address = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password...'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Player
        fields = ['username', 'password', 'bio', 'email_address', 'location', 'birth_date', 'avatar', 'image']


class PlayerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password...'}))
