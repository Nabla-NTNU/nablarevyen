from django.urls import path

from . views import Frontpage

urlpatterns = [
    path('', Frontpage.as_view(), name='index'),
]
