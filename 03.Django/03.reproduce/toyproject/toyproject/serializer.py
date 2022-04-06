from rest_framework import serializers
from gallery.models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'explanation', 'created_at', 'image', 'type']