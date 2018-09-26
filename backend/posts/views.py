"""
Views for Posts
"""

from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    """APIListView for Posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)