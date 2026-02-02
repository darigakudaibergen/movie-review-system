"""
URL Configuration for Movies App
Created by: [Name] - Participant 3
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('top-rated/', views.top_rated, name='top_rated'),
    path('search/', views.search_movies, name='search_movies'),
]
