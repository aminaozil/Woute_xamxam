from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from articles.models import Article
from .forms import AddArticle


def home(request):
    return render(request, "home.html")

@login_required(login_url="connexion")
def add_articles(request):
    form = AddArticle(request.POST, request.FILES)
    if request.method == "POST":
        
        auteur = request.user
        categorie_id = request.POST['categorie']
        img = request.FILES['img']
        titre = request.POST['titre']
        resume = request.POST['resume']
        contenu = request.POST['contenu']

        articles = Article.objects.create(
            auteur = auteur,
            categorie_id = categorie_id,
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
    articles = Article.objects.filter(archive=False)
    #pour la pagination
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    #pour le bouton recherche
    if request.method == "GET":
        name = request.GET.get("recherche")
        if name is not None:
            articles= Article.objects.filter(categorie__icontains=name)
            
    return render(request, "articles/list_article.html", {"articles": articles})


def details_articles(request, id):
    articles = get_object_or_404(Article, id=id)

    dernieres = Article.objects.filter(archive=False).order_by("id")[:3]
    context={
        "articles": articles,
        "dernieres": dernieres

    }
    return render(request, "articles/details_article.html", context)

@login_required(login_url="connexion")
def update_articles(request, id):      
    articles = Article.objects.get(id=id)
    form = AddArticle(request.POST or None, instance=articles)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('/list_articles/')
     
    return render(request, "articles/update_article.html", {"form": form})

@login_required(login_url="connexion")
def delete_articles(request, id):
    articles = get_object_or_404(Article, id=id)
    if request.method == "POST":
        del_articles = Article.objects.filter(pk=articles.id)
        del_articles.update(
            archive = True
            
        )
        redirect("/list_articles/")

    return render(request, "articles/delete_article.html", {"articles": articles})

def derniere_articles(request):
    dernieres = Article.objects.filter(archive=False).order_by("date_updated")[:3]

    return render(request, "articles/derniere_articles.html", {"dernieres": dernieres})