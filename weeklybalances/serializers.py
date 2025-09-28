from rest_framework import serializers
from .models import WeeklyBalance

class WeeklyBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyBalance
        fields = '__all__'
