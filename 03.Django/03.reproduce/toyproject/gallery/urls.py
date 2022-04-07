from django.urls import path
from gallery.views import GalleryViewSet, gallery_root, gallery_list
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

gallery_list = GalleryViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

gallery_detail = GalleryViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('queue/', gallery_list),
]
