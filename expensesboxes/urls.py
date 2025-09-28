from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpensesBoxesViewSet

router = DefaultRouter()
router.register(r'expensesboxes', ExpensesBoxesViewSet, basename='expensesbox')

urlpatterns = [
    path('', include(router.urls)),
]
