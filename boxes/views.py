from rest_framework import viewsets
from .models import Box, Record
from .serializers import BoxSerializer, RecordSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer

    def get_queryset(self):
        queryset = Record.objects.all()
        box_id = self.request.query_params.get('box_id')
        if box_id is not None:
            queryset = queryset.filter(box_id=box_id)
        return queryset
