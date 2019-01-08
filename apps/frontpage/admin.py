from django.contrib import admin
from image_cropping import ImageCroppingMixin
from . models import CarouselItem


class CarouselItemAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'published',)

admin.site.register(CarouselItem, CarouselItemAdmin)
