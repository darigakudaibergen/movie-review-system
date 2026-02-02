"""
Django Admin Configuration for Movie Review System
Created by: [Your Name] - Participant 1
"""
from django.contrib import admin
from .models import Genre, Movie, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin interface for Genre model"""
    list_display = ['name', 'movie_count']
    search_fields = ['name']
    ordering = ['name']
    
    def movie_count(self, obj):
        """Display number of movies in this genre"""
        return obj.movies.count()
    movie_count.short_description = 'Number of Movies'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin interface for Movie model"""
    list_display = [
        'title', 
        'release_year', 
        'director', 
        'genre',
        'average_rating',
        'review_count',
        'created_at'
    ]
    list_filter = ['genre', 'release_year', 'created_at']
    search_fields = ['title', 'director', 'description']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'average_rating', 'review_count']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'director', 'release_year', 'genre')
        }),
        ('Details', {
            'fields': ('description', 'duration_minutes', 'poster_url')
        }),
        ('Statistics', {
            'fields': ('average_rating', 'review_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def average_rating(self, obj):
        """Display average rating"""
        return f"{obj.average_rating}★"
    average_rating.short_description = 'Avg Rating'
    
    def review_count(self, obj):
        """Display review count"""
        return obj.review_count
    review_count.short_description = 'Reviews'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin interface for Review model"""
    list_display = [
        'user',
        'movie',
        'rating',
        'title',
        'created_at'
    ]
    list_filter = ['rating', 'created_at', 'movie']
    search_fields = ['title', 'comment', 'user__username', 'movie__title']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Review Information', {
            'fields': ('movie', 'user', 'rating', 'title')
        }),
        ('Review Content', {
            'fields': ('comment',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# Customize admin site headers
admin.site.site_header = "Movie Review Administration"
admin.site.site_title = "Movie Review Admin"
admin.site.index_title = "Welcome to Movie Review Admin Panel"
