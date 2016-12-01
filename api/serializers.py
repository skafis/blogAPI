from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from .models import Post

post_detail_url = HyperlinkedIdentityField(
	view_name = 'api:detail',
	lookup_field='slug'
	)

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'title',
		'content',
		'created_date',
		]

class PostListSerializer(ModelSerializer):
	url = post_detail_url
	class Meta:
		model = Post
		fields = [
		'url',
		'title',
		'content',
		'published_date',
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		'author',
		'title',
		'content',
		'published_date',
		]