from rest_framework import serializers
from .models import Box, Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    records = RecordSerializer(many=True, read_only=True)

    class Meta:
        model = Box
        fields = ['id', 'name', 'icon', 'total', 'createdAt', 'records']
