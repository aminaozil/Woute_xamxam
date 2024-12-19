from django.shortcuts import render
from articles.models import Article

def propos(request):
    articles = Article.objects.filter(archive=False).order_by("date_updated")[:6]
    return render(request, "details/propos.html", {"articles": articles})

def programmes(request):
    return render(request, "details/programme.html")

def contact(request):
    return render(request, "details/contact.html")