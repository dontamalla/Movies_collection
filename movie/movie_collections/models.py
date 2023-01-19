from django.db import models

# Create your models here.
# movie_collections/models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Collection(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
