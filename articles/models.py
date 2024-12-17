from django.db import models
from django.contrib.auth.models import User




class Article(models.Model):
    categorie_select = [
                    ("DEVELOPPEMENT WEB", "DEVELOPPEMENT WEB"), 
                    ("MARKETING DIGITAL", "MARKETING DIGITAL"), 
                    ("DEVELOPPEMENT MOBILE", "DEVELOPPEMENT MOBILE"), 
    ]
    categorie = models.CharField(choices= categorie_select, max_length=255, null=True, blank=True)
    titre = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    resume = models.CharField(max_length=255)
    contenu = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)


    class Meta:
        ordering = ['date_updated']

    

