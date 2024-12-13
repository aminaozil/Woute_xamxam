from django.contrib import messages
from django.shortcuts import redirect, render
from .form import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/list_articles/")
        else: 
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, "utilisateurs/login.html")

def register_form(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/connexion/")
    else:
        form = CustomUserCreationForm()
    return render(request, "utilisateurs/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/connexion/")