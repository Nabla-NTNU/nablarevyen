from django.urls import path

from . views import ArchiveList, ArchiveDetail

urlpatterns = [
    path('', ArchiveList.as_view(), name='list'),
    path('<slug:slug>/', ArchiveDetail.as_view(), name='detail'),
]
