from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping import ImageRatioField


# Create your models here.
class Article(models.Model):
    published = models.BooleanField(
        help_text="Set this when article is ready to be published."
    )
    pinned = models.BooleanField(
        help_text="Pin this article to the frontpage.<br/>Multiple pinned articles are sorted by date."
    )
    deny_frontpage = models.BooleanField(
        help_text="Set this to deny this article to be displayed on the frontpage."
    )
    slug = models.SlugField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="articles/%Y/",
        help_text="To crop the image, simply click save and continue.",
    )
    desktop_crop = ImageRatioField("image", "600x300", size_warning=True)
    mobile_crop = ImageRatioField("image", "600x400", size_warning=True)
    keywords = models.CharField(
        max_length=60,
        blank=True,
        help_text="Keywords used for search engine optimalization.",
    )
    summary = models.TextField(
        max_length=200, help_text="Short summary on maximum of 200 words."
    )
    content = RichTextUploadingField()
    last_changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse("people.views.details", args=[str(self.id)])
