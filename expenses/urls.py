from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpensesViewSet

router = DefaultRouter()
router.register(r'expenses', ExpensesViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]