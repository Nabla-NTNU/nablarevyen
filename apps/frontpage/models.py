from django.db import models
from django.urls import reverse
from image_cropping import ImageRatioField


class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel/', help_text="To crop the image, simply click save and continue.")
    desktop_crop = ImageRatioField('image', '2000x300', size_warning=True)
    mobile_crop = ImageRatioField('image', '600x600', size_warning=True)
    link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return '%s' % (self.title)
