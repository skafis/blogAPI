from django.conf.urls import url

from . views import (
	PostListAPIView
	)

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]
