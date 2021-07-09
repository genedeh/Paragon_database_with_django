from django.db import models
from game.models import Avatar


class Player(models.Model):
    username = models.CharField(max_length=299, unique=True)
    password = models.CharField(max_length=20, help_text="Must have up to 8 characters", unique=True)
    email_address = models.EmailField()
    bio = models.TextField(max_length=500, blank=True, default="")
    location = models.CharField(max_length=30, help_text="Make sure it is a valid country or city")
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"


class Group(models.Model):
    name = models.CharField(max_length=369, unique=True)
    leader = models.OneToOneField("Player", on_delete=models.CASCADE, unique=True, primary_key=True,
                                  related_name="+")
    defender = models.OneToOneField("Player", on_delete=models.CASCADE, default="", unique=True, blank=True,
                                    related_name="+", null=True)
    middlemen = models.OneToOneField("Player", on_delete=models.CASCADE, default="", unique=True, blank=True,
                                     related_name="+", null=True)
    capturer = models.OneToOneField("Player", on_delete=models.CASCADE, default="", unique=True, blank=True,
                                    related_name='+', null=True)
    logo = models.ImageField(unique=True)
    doc = models.TextField(unique=True, verbose_name="Documentation")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Friend(models.Model):
    name = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='+')
    friend = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"{self.friend}"
