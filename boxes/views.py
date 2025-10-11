from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone # Import timezone
from django.conf import settings # Import Django settings
from .models import Box, BoxControls
from .serializers import BoxSerializer, BoxControlsSerializer

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all() # Box model does not have deletedAt, so no filter here
    serializer_class = BoxSerializer

class BoxControlsViewSet(viewsets.ModelViewSet):
    queryset = BoxControls.objects.filter(deletedAt__isnull=True) # Filter out soft-deleted items
    serializer_class = BoxControlsSerializer

    def get_queryset(self):
        box_id = self.request.query_params.get('box_id')
        if box_id is None:
            if self.request.user.is_superuser:
                return BoxControls.objects.all()
            if getattr(settings, 'DEBUG', False):
                return BoxControls.objects.all()
            return BoxControls.objects.none() # Return empty queryset if no box_id is provided
        queryset = BoxControls.objects.filter(box_id=box_id)
        only_deleted = self.request.query_params.get('only_deleted')
        if only_deleted is not None:
            queryset = BoxControls.objects.filter(deletedAt__isnull=True) # Ensure filter is applied here too
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deletedAt = timezone.now() # Soft delete
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
