from rest_framework import viewsets
from .models import WeeklyBalance
from .serializers import WeeklyBalanceSerializer

class WeeklyBalanceViewSet(viewsets.ModelViewSet):
    queryset = WeeklyBalance.objects.all()
    serializer_class = WeeklyBalanceSerializer