from django.db import models
from django.contrib.auth.models import User




class Article(models.Model):
    categorie = models.CharField(max_length=255)
    titre = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    resume = models.CharField(max_length=255)
    contenu = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)



