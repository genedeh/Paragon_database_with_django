from django.contrib import admin
from .models import Player, Group


# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "avatar", "birth_date", "location")
    prepopulated_fields = {
        'slug': ['username']
    }
    autocomplete_fields = ['avatar']


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "updated")


admin.site.register(Player, PlayerAdmin)
admin.site.register(Group, GroupAdmin)
