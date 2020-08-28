from rest_framework import serializers
from fullstack.models import image
class imageSerializer(serializers.Serializer):
    img=serializers.ImageField()
    def create(self,validated_data):
        return image.objects.create(**validated_data)