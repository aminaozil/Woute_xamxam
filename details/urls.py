from django.urls import path
from .views import propos, programmes, contact, list_contact

urlpatterns = [
    path("about/", propos, name="about"),
    path("nosprogrammes/", programmes, name="nosprogrammes"),
    path("add_contact/", contact, name="contacts"),
    path("contact/", list_contact, name="contact"),

]
