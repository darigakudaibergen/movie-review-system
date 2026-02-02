"""
API Views for Movie Review System
Created by: [Name] - Participant 4
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Movie, Review, Genre
from .serializers import (
    MovieSerializer, 
    MovieListSerializer,
    ReviewSerializer, 
    GenreSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint for genres
    GET /api/genres/ - List all genres
    POST /api/genres/ - Create new genre
    GET /api/genres/{id}/ - Get specific genre
    PUT /api/genres/{id}/ - Update genre
    DELETE /api/genres/{id}/ - Delete genre
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for movies
    GET /api/movies/ - List all movies
    POST /api/movies/ - Create new movie
    GET /api/movies/{id}/ - Get specific movie with reviews
    PUT /api/movies/{id}/ - Update movie
    DELETE /api/movies/{id}/ - Delete movie
    GET /api/movies/top_rated/ - Get top rated movies
    """
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        """Use different serializers for list and detail views"""
        if self.action == 'list':
            return MovieListSerializer
        return MovieSerializer
    
    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        """Get top rated movies"""
        movies = Movie.objects.all()
        
        # Calculate ratings and sort
        movies_with_ratings = [
            {
                'movie': movie,
                'average_rating': movie.average_rating,
                'review_count': movie.review_count
            }
            for movie in movies if movie.review_count > 0
        ]
        
        movies_with_ratings.sort(
            key=lambda x: x['average_rating'], 
            reverse=True
        )
        
        # Get top 20 movies
        top_movies = [item['movie'] for item in movies_with_ratings[:20]]
        
        serializer = MovieListSerializer(top_movies, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Get all reviews for a specific movie"""
        movie = self.get_object()
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint for reviews
    GET /api/reviews/ - List all reviews
    POST /api/reviews/ - Create new review (requires authentication)
    GET /api/reviews/{id}/ - Get specific review
    PUT /api/reviews/{id}/ - Update review (only own review)
    DELETE /api/reviews/{id}/ - Delete review (only own review)
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Set user to current user when creating review"""
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        """Only allow users to update their own reviews"""
        if serializer.instance.user != self.request.user:
            return Response(
                {'error': 'You can only update your own reviews'},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save()
    
    def perform_destroy(self, instance):
        """Only allow users to delete their own reviews"""
        if instance.user != self.request.user:
            return Response(
                {'error': 'You can only delete your own reviews'},
                status=status.HTTP_403_FORBIDDEN
            )
        instance.delete()
    
    @action(detail=False, methods=['get'])
    def my_reviews(self, request):
        """Get reviews by current user"""
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        reviews = Review.objects.filter(user=request.user)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)
