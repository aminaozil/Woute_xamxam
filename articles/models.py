from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    titre = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/')
    resume = models.CharField(max_length=255)
    contenu = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titre}"
    



    

    

