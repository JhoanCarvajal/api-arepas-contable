from rest_framework import viewsets
from .models import History
from .serializers import HistorySerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer