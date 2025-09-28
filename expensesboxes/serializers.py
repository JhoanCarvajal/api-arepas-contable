from rest_framework import serializers
from .models import ExpensesBoxes

class ExpensesBoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesBoxes
        fields = '__all__'
