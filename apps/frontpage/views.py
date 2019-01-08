from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from ..articles.models import Article

class Frontpage(View):
    def get(self, request):
        article_list = Article.objects.filter(published=True, deny_frontpage=False).order_by('-pinned', 'created')[:3]
        return render(request, 'frontpage/frontpage.html', {'article_list': article_list})
