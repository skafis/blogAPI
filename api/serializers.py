from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)
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
	user = SerializerMethodField()

	class Meta:
		model = Post
		fields = [
		'url',
		'user',
		'title',
		'content',
		'published_date',
		]

	def get_user(self, instance):
		return str(instance.author.username)

class PostDetailSerializer(ModelSerializer):
	user = SerializerMethodField()
	image = SerializerMethodField()
	# markdown = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
		'user',
		'title',
		'content',
		# 'markdown',
		'published_date',
		'image'
		]

	def get_user(self, instance):
		return str(instance.author.username)

	def get_image(self, instance):
		try:
			image = instance.image.url
		except:
			image = None
		return image

	# def get_html(self, instance):
	# 	return instance.get_markdown()