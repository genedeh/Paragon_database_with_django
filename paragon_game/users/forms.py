from django import forms
from django.forms import ModelForm
from .models import Player


class PlayerSigninForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))
    password = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Player
        fields = '__all__'
        error_messages = {
            'password': {
                'max_length': "Password must not pass 20 characters",
            },
        }
