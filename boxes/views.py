from rest_framework import viewsets
from .models import Box, BoxControls
from .serializers import BoxSerializer, BoxControlsSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class BoxControlsViewSet(viewsets.ModelViewSet):
    serializer_class = BoxControlsSerializer

    def get_queryset(self):
        queryset = BoxControls.objects.all()
        box_id = self.request.query_params.get('box_id')
        if box_id is not None:
            queryset = queryset.filter(box_id=box_id)
        return queryset