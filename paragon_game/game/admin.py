from django.contrib import admin
from .models import Avatar, Bloodline


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('bloodline', 'power', 'name')


# Register your models here.
admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Bloodline)
# headers and titles
admin.site.site_header = 'PARAGON ADMIN PANEL'
admin.site.site_title = 'PARAGON GAME SITE ADMIN'
admin.site.index_title = 'GAME ADMINISTRATION'
