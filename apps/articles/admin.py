from django.contrib import admin
from image_cropping import ImageCroppingMixin
from . models import Article


class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'published', 'deny_frontpage', 'pinned')

admin.site.register(Article, ArticleAdmin)
