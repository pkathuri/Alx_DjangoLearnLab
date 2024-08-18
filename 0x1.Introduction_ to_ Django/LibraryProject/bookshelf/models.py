from django.db import models

# Create your models here.
class Book(models.model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publication_year = models.IntegerField()