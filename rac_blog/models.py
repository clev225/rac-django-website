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


# Add this to your existing models.py file

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


class Service(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_published = models.DateField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    descriptions_json = models.TextField(default='[]')  # Store descriptions as JSON
    requirements_json = models.TextField(default='[]')  # Store requirements as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def descriptions(self):
        try:
            return json.loads(self.descriptions_json)
        except:
            return []
    
    @descriptions.setter
    def descriptions(self, value):
        self.descriptions_json = json.dumps(value)
    
    @property
    def requirements(self):
        try:
            return json.loads(self.requirements_json)
        except:
            return []
    
    @requirements.setter
    def requirements(self, value):
        self.requirements_json = json.dumps(value)
    
    def __str__(self):
        return self.title
