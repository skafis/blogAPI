# from django.shortcuts import render
from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView
	)

from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer
# Create your views here.

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'