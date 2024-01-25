from django.urls import path
from .views import BounceView

urlpatterns = [
    path("", BounceView.as_view()),
]
