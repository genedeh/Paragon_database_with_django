from django.db import models


# Create your models here.

class Avatar(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField()
    power = models.CharField(max_length=359)
    bio = models.TextField()
    bloodline = models.ForeignKey('Bloodline', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Bloodline(models.Model):
    name = models.CharField(max_length=159, unique=True)
    power_level = models.FloatField(unique="True")
    symbol = models.ImageField()

    def __str__(self):
        return f"{self.name}"
