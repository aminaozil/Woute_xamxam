from django.shortcuts import redirect, render
from .form import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def login_form(request):
   
   
    return render(request, "utilisateurs/login.html", {})

def register_form(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/list_articles/")
    else:
        form = CustomUserCreationForm()
    return render(request, "utilisateurs/register.html", {"form": form})