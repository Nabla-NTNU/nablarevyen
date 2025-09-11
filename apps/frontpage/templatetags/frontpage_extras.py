from datetime import datetime
from django import template
from django.utils import timezone

register = template.Library()


@register.filter(name="unix_to_datetime")
def unix_to_datetime(value):
    dt = datetime.fromtimestamp(int(value))
    return timezone.make_aware(dt, timezone.get_default_timezone())
