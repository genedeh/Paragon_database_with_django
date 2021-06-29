from django import forms
from django.db import models
from django.contrib.auth.models import User
from game.models import Avatar
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.EmailField()
    bio = models.TextField(max_length=500, blank=True, default="")
    location = models.CharField(max_length=30, help_text="Make sure it is a valid country or city")
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


class Player(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20, help_text="Must have upto 8 characters")
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
