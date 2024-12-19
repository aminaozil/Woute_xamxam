from django.db import models
from  django.contrib.auth.models import User


class Contact(models.Model):
    sujet = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    
