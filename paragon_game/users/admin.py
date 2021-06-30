from django.contrib import admin
from .models import  Player


# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "avatar", "birth_date", "location")

admin.site.register(Player, PlayerAdmin)
