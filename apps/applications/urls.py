from django.urls import path

from .views import ApplicationView, ApplicationSuccessView

urlpatterns = [
    path("", ApplicationView.as_view(), name="index"),
    path("suksess/", ApplicationSuccessView.as_view(), name="success"),
]
