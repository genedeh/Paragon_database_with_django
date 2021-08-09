from django.db import models
from game.models import Avatar
from django_countries.fields import CountryField
import random
import string


class Player(models.Model):
    username = models.CharField(max_length=299, unique=True)
    password = models.CharField(max_length=20, help_text="Must have up to 8 - 20 characters", unique=True)
    email_address = models.EmailField()
    bio = models.TextField(max_length=500, blank=True, default="")
    location = CountryField(blank_label='(SELECT YOUR COUNTRY/LOCATION)')
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"


class Group(models.Model):
    name = models.CharField(max_length=369, unique=True)
    leader = models.OneToOneField("Player", on_delete=models.PROTECT, unique=True, primary_key=True,
                                  related_name="+")
    defender = models.OneToOneField("Player", on_delete=models.PROTECT, default="", unique=True, blank=True,
                                    related_name="+", null=True)
    middlemen = models.OneToOneField("Player", on_delete=models.PROTECT, default="", unique=True, blank=True,
                                     related_name="+", null=True)
    capturer = models.OneToOneField("Player", on_delete=models.PROTECT, default="", unique=True, blank=True,
                                    related_name='+', null=True)
    logo = models.ImageField(unique=True)
    doc = models.TextField(unique=True, verbose_name="Documentation")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Friend(models.Model):
    name = models.CharField(max_length=245)
    friend = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.friend} is  a friend to {self.name}"


class Message(models.Model):
    From = models.CharField(max_length=249)
    To = models.ForeignKey(Friend, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"This message is from {self.From} and to {self.To.friend}"
