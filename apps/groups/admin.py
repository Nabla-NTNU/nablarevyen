from django.contrib import admin
from .models import Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "published")


admin.site.register(Group, GroupAdmin)
