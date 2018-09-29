"""
Views for Posts
"""

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post
from .serializers import PostSerializer, PostCreateSerializer

class PostList(generics.ListAPIView):
    """APIListView for Posts"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    """Detail view for Post"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)

class PostCreate(generics.CreateAPIView):
    """Create a new post"""
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = None