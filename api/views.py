# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from . models import Post
# Create your views here.

class PostListAPIView(ListAPIView):
	querset = Post.objects.all()