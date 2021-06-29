from django.contrib import admin
from .models import Profile, Player


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'email_address', 'location')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "avatar", "profile")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Player, PlayerAdmin)
