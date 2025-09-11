from django.db import models
from django.urls import reverse
from image_cropping import ImageRatioField


class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(
        default=False, help_text="Set this to publish carousel item."
    )
    image = models.ImageField(
        upload_to="carousel/",
        help_text="To crop the image, simply click save and continue.",
    )
    desktop_crop = ImageRatioField("image", "2000x600", size_warning=True)
    mobile_crop = ImageRatioField("image", "600x500", size_warning=True)
    link = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.title)

    class Meta:
        verbose_name = "Carousel item"
        verbose_name_plural = "Carousel items"
