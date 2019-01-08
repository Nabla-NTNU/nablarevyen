from django.views.generic import ListView, DetailView
from . models import Article

class ArticleList(ListView):
    model = Article
    queryset = Article.objects.filter(published=True).order_by('created')
    paginate_by = 12
    page_kwarg = 'side'


class ArticleDetail(DetailView):
    model = Article
