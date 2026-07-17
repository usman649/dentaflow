from rest_framework import serializers
from apps.authentication.models import Gallery


class GalleryListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()

class GalleryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = [
            'id',
            'user',
            'image',
        ]