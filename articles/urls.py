from .views import add_articles, home, list_articles, details_articles, update_articles
from django.urls import path


urlpatterns = [
    path("", home, name="home"),
    path("add_articles/", add_articles, name="add_articles"),
    path("list_articles/", list_articles, name="list_articles"),
    path("details_articles/", details_articles, name="details_articles"),
    path("update_articles/", update_articles, name="update_articles")
]
