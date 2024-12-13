# Generated by Django 5.1.4 on 2024-12-13 22:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=255)),
                ('titre', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='images/')),
                ('resume', models.CharField(max_length=255)),
                ('contenu', models.TextField()),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
