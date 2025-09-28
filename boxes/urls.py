from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoxViewSet, BoxControlsViewSet

router = DefaultRouter()
router.register(r'boxes', BoxViewSet, basename='box')
router.register(r'boxcontrols', BoxControlsViewSet, basename='boxcontrol')

urlpatterns = [
    path('', include(router.urls)),
]