from django.contrib import admin
from . models import Position, Application


class PositionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'published', 'deadline',)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'name',)
    list_filter = ('position',)


admin.site.register(Position, PositionAdmin)
admin.site.register(Application, ApplicationAdmin)
