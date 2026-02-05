
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import MovieViewSet, ReviewViewSet, GenreViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
]
