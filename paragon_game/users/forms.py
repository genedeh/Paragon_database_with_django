from django import forms
from django.forms import ModelForm

from .models import Player


class PlayerSigninForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Player
        fields = '__all__'
