from django.db import models
from django.urls import reverse
from image_cropping import ImageRatioField
from embed_video.fields import EmbedVideoField


class Archive(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    display_in_menu = models.BooleanField(
        help_text='Set this to display in the archive menu. Otherwise found under "Read more"'
    )
    published = models.BooleanField(help_text="Set this to publish the entire archive")
    keywords = models.CharField(max_length=200)
    description = models.TextField(
        max_length=2000, help_text="Short description of the archive, 2000 symbols."
    )
    thumbnail_image = models.ImageField(
        upload_to="archive/archive/",
        help_text="To crop the image, simply click save and continue.",
    )
    thumbnail_image_crop = ImageRatioField(
        "thumbnail_image", "400x400", size_warning=True
    )

    def __str__(self):
        return "%s" % (self.name)


class Image(models.Model):
    archive = models.ForeignKey("Archive", on_delete=models.CASCADE)
    alt = models.CharField(max_length=50)
    description = models.TextField(
        max_length=200, help_text="Short description of the image, 200 symbols."
    )
    image = models.ImageField(
        upload_to="archive/images/",
        help_text="To crop the image, simply click save and continue.",
    )
    image_crop = ImageRatioField("image", "400x400", size_warning=True)

    def __str__(self):
        return "%s" % (self.alt)


class Video(models.Model):
    archive = models.ForeignKey("Archive", on_delete=models.CASCADE)
    alt = models.CharField(max_length=50)
    description = models.TextField(
        max_length=200, help_text="Short description of the video, 200 symbols."
    )
    link = EmbedVideoField()

    def __str__(self):
        return "%s" % (self.alt)
