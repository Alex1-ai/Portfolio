from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)