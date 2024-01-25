from django.views.generic import View
from django.shortcuts import redirect
from django.views.static import HttpResponse

from .models import Bounce


class BounceView(View):
    def get(self, request):
        bounce_instance = Bounce.objects.first()
        if bounce_instance is None:
            return HttpResponse("Her var det ingenting :(")
        url = bounce_instance.url
        return redirect(url)
