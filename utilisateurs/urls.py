from django.urls import path
from .views import login_form, register_form, logout_view

urlpatterns = [
    path("connexion/", login_form, name="connexion"),
    path("inscription/", register_form, name="inscription"),
    path("deconnexion/", logout_view, name="deconnexion"),

]
