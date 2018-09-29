"""
Serializers for Post Model
"""

from rest_framework import serializers
from . import models

class PostCreateSerializer(serializers.ModelSerializer):
    """
    Post Creation Serializer
    """
    class Meta:
        """Meta Class"""
        fields = ('title', 'content')
        model = models.Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta Class"""
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post



class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('uploaded_at', 'upload',)
        model = models.Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('uploaded_at', 'upload')
        model = models.Document
