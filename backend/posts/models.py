"""
Models for the posts app
"""

from django.db import models

class Post(models.Model):
    """Post model for demonstration"""
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Document(models.Model):
    """Document model for demonstration"""
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
