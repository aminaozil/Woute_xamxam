from django.urls import path
from .views import propos, programmes

urlpatterns = [
    path("about/", propos, name="about"),
    path("nosprogrammes/", programmes, name="nosprogrammes"),
]
