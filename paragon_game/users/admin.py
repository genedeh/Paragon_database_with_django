from django.contrib import admin
from .models import Player, Group, Friend, Message


# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("username", "avatar", "birth_date", "location")
    prepopulated_fields = {
        'slug': ['username']
    }
    autocomplete_fields = ['avatar']


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "updated")


# class MemberAdmin(admin.ModelAdmin):
#     list_display = ("name", "group_name")


admin.site.register(Player, PlayerAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Friend)
admin.site.register(Message)
# admin.site.register(Member, MemberAdmin)
