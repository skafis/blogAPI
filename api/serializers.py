from rest_framework.serializers import ModelSerializer

from .models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'title',
		'content',
		'created_date',
		]

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
		'author',
		'title',
		'slug',
		'content',
		'created_date',
		'published_date',
		]