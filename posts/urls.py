from django.conf.urls import url
from .views import post_create, post_delete, post_detail, post_list, post_update

urlpatterns = [
    url(r'^$', post_list, name='post-list'),
    url(r'^create/$', post_create, name='post-create'),
    url(r'^(?P<pk>\d+)/edit/$', post_update, name='post-edit'),
    url(r'^(?P<pk>\d+)/delete/$', post_delete, name='post-delete'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post-detail'),
]
