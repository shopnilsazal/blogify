from django.conf.urls import url
from .views import post_create, post_delete, post_detail, post_list, post_update, post_category, post_tags

urlpatterns = [
    url(r'^$', post_list, name='post-list'),
    url(r'^create/$', post_create, name='post-create'),
    url(r'^category/(?P<slug>[^\.]+)/$', post_category, name='post-category'),
    url(r'^tag/(?P<slug>[^\.]+)/$', post_tags, name='post-tag'),
    url(r'^(?P<slug>[^\.]+)/edit/$', post_update, name='post-edit'),
    url(r'^(?P<slug>[^\.]+)/delete/$', post_delete, name='post-delete'),
    url(r'^(?P<slug>[^\.]+)/$', post_detail, name='post-detail'),
]
