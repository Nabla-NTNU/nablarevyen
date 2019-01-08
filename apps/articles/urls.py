from django.urls import path

from . views import ArticleList, ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view(), name='list'),
    path('<slug:slug>/', ArticleDetail.as_view(), name='detail'),
]
