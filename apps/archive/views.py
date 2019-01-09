from django.views.generic import ListView, DetailView
from . models import Archive

class ArchiveList(ListView):
    model = Archive
    queryset = Archive.objects.filter(published=True).order_by('name')
    paginate_by = 12
    page_kwarg = 'side'

class ArchiveDetail(DetailView):
    model = Archive
    queryset = Archive.objects.filter(published=True)
