from django.shortcuts import render, redirect
from articles.models import Article
from details.models import Contact
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def propos(request):
    articles = Article.objects.filter(archive=False).order_by("date_updated")[:4]
    paginator = Paginator(articles, 6)
    page = request.GET.get('page')
    arts = paginator.get_page(page)
    if request.method == "GET":
        name = request.GET.get("recherche")
        if name is not None:
            articles = Article.objects.filter(categorie__icontains=name)
    return render(request, "details/propos.html", {"arts": arts, "articles":articles})

def programmes(request):
    return render(request, "details/programme.html")

def contact(request):
    
    if request.method == "POST":
        
        sujet = request.POST['sujet']
        email = request.POST['email']
        description = request.POST['description']
        contact = Contact.objects.create(
            
            sujet = sujet,
            email = email,
            description = description,
        )
        
        contact.save()
        
        redirect("/contact/")
        
    return render(request, "details/contact.html")

@login_required(login_url="connexion")
def list_contact(request):
    contacts = Contact.objects.all()
    return render(request, "details/contact_list.html", {"contacts":contacts})