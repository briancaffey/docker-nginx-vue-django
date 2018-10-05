"""
Views for Posts
"""
import random

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny #, IsAuthenticated
from rest_framework.response import Response
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post, Document
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    DocumentCreateSerializer,
    DocumentSerializer
)

@api_view()
def random_nubers(request): #pylint: disable=unused-argument
    """Sample data call"""
    data = random.sample(range(1, 100), 15)
    json = {"data": data}
    return Response(json)

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


class DocumentCreate(generics.CreateAPIView):
    """Create a new document"""
    queryset = Document.objects.all()
    serializer_class = DocumentCreateSerializer
    permission_classes = (AllowAny,)


class DocumentListView(generics.ListAPIView):
    """List View for Documents"""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (AllowAny,)
