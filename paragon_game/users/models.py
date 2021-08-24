from django.db import models
from django.urls import reverse
from game.models import Avatar
from django_countries.fields import CountryField


class Player(models.Model):

    def user_name(self):
        return self.username

    username = models.CharField(max_length=299, unique=True, null=True)
    slug = models.SlugField(blank=True)
    password = models.CharField(max_length=20, help_text="Must have up to 8 - 20 characters", unique=True)
    email_address = models.EmailField()
    bio = models.TextField(blank=True, default="", null=True)
    location = CountryField(blank_label='SELECT YOUR LOCATION....', blank=True)
    birth_date = models.DateField(null=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse('users:player', kwargs={'slug': self.slug})


class Group(models.Model):
    name = models.CharField(max_length=369, unique=True)
    leader = models.OneToOneField("Player", on_delete=models.PROTECT, unique=True, primary_key=True,
                                  related_name='leader')
    defender = models.OneToOneField("Player", on_delete=models.PROTECT, default="", unique=True, blank=True,
                                    related_name="defender", null=True)
    middlemen = models.OneToOneField("Player", on_delete=models.PROTECT, default="", unique=True, blank=True,
                                     related_name="middlemen", null=True)
    capturer = models.OneToOneField("Player", on_delete=models.PROTECT, default="", unique=True, blank=True,
                                    related_name='capturer', null=True)
    logo = models.ImageField()
    doc = models.TextField(unique=True, verbose_name="Documentation")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
