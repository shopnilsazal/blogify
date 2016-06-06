from django.conf.urls import url
from .views import post_create, post_delete, post_detail, post_list, post_update

urlpatterns = [
    url(r'^$', post_list, name='post-list'),
    url(r'^create/$', post_create, name='post-create'),
    url(r'^detail/$', post_detail, name='post-detail'),
    url(r'^update/$', post_update, name='post-update'),
    url(r'^delete/$', post_delete, name='post-delete'),
]
