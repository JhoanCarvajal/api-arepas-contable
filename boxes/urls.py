from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoxViewSet, RecordViewSet

router = DefaultRouter()
router.register(r'boxes', BoxViewSet, basename='box')
router.register(r'records', RecordViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),
]
