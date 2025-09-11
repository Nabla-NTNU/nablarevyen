from django.contrib import admin
from image_cropping import ImageCroppingMixin
from embed_video.admin import AdminVideoMixin
from .models import Archive, Image, Video


class ArchiveAdmin(ImageCroppingMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "slug",
        "published",
        "display_in_menu",
    )


class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "archive",
        "alt",
    )


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = (
        "id",
        "archive",
        "alt",
    )


admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
