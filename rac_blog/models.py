from django.db import models
import json

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    description = models.TextField()
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='announcements/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
