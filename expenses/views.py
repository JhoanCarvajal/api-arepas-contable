from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone # Import timezone
from .models import Expenses
from .serializers import ExpensesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.filter(deletedAt__isnull=True) # Filter out soft-deleted items
    serializer_class = ExpensesSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deletedAt = timezone.now() # Soft delete
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)