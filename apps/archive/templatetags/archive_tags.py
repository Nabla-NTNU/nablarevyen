from django import template

register = template.Library()

from ..models import Archive


@register.simple_tag
def archive_menu():
    archive_list = Archive.objects.filter(
        published=True, display_in_menu=True
    ).order_by("name")
    return archive_list
