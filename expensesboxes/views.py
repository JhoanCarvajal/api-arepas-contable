from rest_framework import viewsets
from .models import ExpensesBoxes
from .serializers import ExpensesBoxesSerializer

class ExpensesBoxesViewSet(viewsets.ModelViewSet):
    queryset = ExpensesBoxes.objects.all()
    serializer_class = ExpensesBoxesSerializer