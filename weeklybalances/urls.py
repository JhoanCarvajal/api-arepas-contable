from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeeklyBalanceViewSet

router = DefaultRouter()
router.register(r'weeklybalances', WeeklyBalanceViewSet, basename='weeklybalance')

urlpatterns = [
    path('', include(router.urls)),
]
