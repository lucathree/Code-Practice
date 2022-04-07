from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from gallery.models import Gallery
from gallery.serializer import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


### API Root endpoint
@api_view(['GET'])
def gallery_root(request, format=None):
    return Response({
        'gallery': reverse('gallery-list', request=request, format=format)
    })


import django_rq
from redis import Redis

queue = django_rq.get_queue('default')

@api_view(['GET', 'POST'])
def gallery_list(request, format=None):
    if request.method == 'GET':
        image = Gallery.objects.all()
        serializer = GallerySerializer(image, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return queue.enqueue(Response(serializer.data, status=status.HTTP_201_CREATED))
        return Response(sserializer.errors, status=status.HTTP_400_BAD_REQUEST)