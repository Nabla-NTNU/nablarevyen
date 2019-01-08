from django.shortcuts import render
from django.views import View

from ..groups.models import Group

class AboutUs(View):
    def get(self, request):
        group_list = Group.objects.filter(published=True)
        return render(request, 'about/about-us.html',{'group_list': group_list})
