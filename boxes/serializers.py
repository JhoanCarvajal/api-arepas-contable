from rest_framework import serializers
from .models import Box, BoxControls

class BoxControlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxControls
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    controls = BoxControlsSerializer(many=True, read_only=True)

    class Meta:
        model = Box
        fields = ['id', 'name', 'icon', 'total', 'cantPriceFields', 'createdAt', 'controls']