from .views import (add_articles, home, list_articles,
                     details_articles, update_articles, delete_articles)
from django.urls import path



urlpatterns = [
    path("", list_articles, name="home"),
    path("list_articles/", list_articles, name="list_articles"),
    path("add_articles/", add_articles, name="add_articles"),
    path("details_articles/<int:id>/", details_articles, name="details_articles"),
    path("update_articles/<int:id>/", update_articles, name="update_articles"),
    path("delete_articles/<int:id>/", delete_articles, name="delete_articles")
]
 
