from rest_framework.serializers import ModelSerializer

from .models import Post

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'id',
		'title',
		'slug',
		'content',
		'published_date',
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'id',
		'title',
		'slug',
		'content',
		'published_date',
		]