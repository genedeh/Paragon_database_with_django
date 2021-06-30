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
