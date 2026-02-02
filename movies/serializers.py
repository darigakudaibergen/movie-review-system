"""
API Serializers for Movie Review System
Created by: [Name] - Participant 4
"""
from rest_framework import serializers
from .models import Movie, Review, Genre
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model"""
    movie_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description', 'movie_count']
    
    def get_movie_count(self, obj):
        return obj.movies.count()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    user = UserSerializer(read_only=True)
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 
            'movie', 
            'movie_title',
            'user', 
            'rating', 
            'title', 
            'comment', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model"""
    genre = GenreSerializer(read_only=True)
    genre_id = serializers.IntegerField(write_only=True, required=False)
    average_rating = serializers.FloatField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'release_year',
            'director',
            'duration_minutes',
            'genre',
            'genre_id',
            'poster_url',
            'average_rating',
            'review_count',
            'reviews',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class MovieListSerializer(serializers.ModelSerializer):
    """Simplified serializer for movie lists (without reviews)"""
    genre = GenreSerializer(read_only=True)
    average_rating = serializers.FloatField(read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'release_year',
            'director',
            'duration_minutes',
            'genre',
            'poster_url',
            'average_rating',
            'review_count',
            'created_at'
        ]
