"""
Serializers for Post Model
"""

from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer
    """

    class Meta:
        """Meta Class"""
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Post
