from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    published = models.BooleanField(default=False, help_text="Set this to make group public.")
    content = RichTextUploadingField()

    def __str__(self):
        return '%s' % (self.name)
