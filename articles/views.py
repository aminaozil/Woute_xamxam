from django.shortcuts import render, redirect

from articles.models import Article
from .forms import AddArticle


def home(request):
    return render(request, "home.html")


def add_articles(request):
    form = AddArticle(request.POST, request.FILES)
    if request.method == "POST":
        
        auteur = request.user
        categorie = request.POST['categorie']
        img = request.POST['img']
        titre = request.POST['titre']
        resume = request.POST['resume']
        contenu = request.POST['contenu']

        articles = Article.objects.create(
            auteur = auteur,
            categorie = categorie,
            img = img,
            titre = titre,
            resume = resume,
            contenu = contenu
            )

        articles.save()
        return redirect("/list_articles/")
    form = AddArticle()      
    return render(request, "articles/add_article.html", {"form":form})

def list_articles(request):
    articles = Article.objects.all()
    return render(request, "articles/list_article.html", {"articles": articles})

def details_articles(request):
    return render(request, "articles/details_article.html")

def update_articles(request):
    return render(request, "articles/update_article.html")

def delete_articles(request):
    return render(request, "articles/delete_article.html")
