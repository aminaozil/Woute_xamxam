from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def add_articles(request):
    return render(request, "articles/add_article.html")

def list_articles(request):
    return render(request, "articles/list_article.html")

def details_articles(request):
    return render(request, "articles/details_article.html")

def update_articles(request):
    return render(request, "articles/update_article.html")

def delete_articles(request):
    return render(request, "articles/delete_article.html")
