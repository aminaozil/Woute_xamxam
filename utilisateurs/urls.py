from django.urls import path
from .views import login_form, register_form

urlpatterns = [
    path("login/", login_form, name="login"),
    path("inscription/", register_form, name="inscription")
]
