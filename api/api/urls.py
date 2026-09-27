from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register('games', GameViewSet, basename='game')

urlpatterns = [
    path('api/', include(router.urls)),
]