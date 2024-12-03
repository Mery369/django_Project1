from django.db import models

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    image = models.URLField()
    text = models.TextField()

def __str__(self) :
    return self.headline