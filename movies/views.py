"""
Views for Movie Review System
Created by: [Name] - Participant 3
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from .models import Movie, Review, Genre
from .forms import ReviewForm


def home(request):
    """
    Home page showing all movies with filters
    """
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    
    # Filter by genre if specified
    genre_filter = request.GET.get('genre')
    if genre_filter:
        movies = movies.filter(genre__id=genre_filter)
    
    # Sort options
    sort_by = request.GET.get('sort', '-created_at')
    if sort_by == 'rating':
        # Sort by average rating (calculated in template/frontend)
        movies = sorted(movies, key=lambda x: x.average_rating, reverse=True)
    elif sort_by == 'year':
        movies = movies.order_by('-release_year')
    else:
        movies = movies.order_by(sort_by)
    
    context = {
        'movies': movies,
        'genres': genres,
        'selected_genre': genre_filter,
        'sort_by': sort_by
    }
    return render(request, 'movies/home.html', context)


def movie_detail(request, movie_id):
    """
    Movie detail page with reviews
    """
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all().select_related('user')
    
    # Check if current user has already reviewed this movie
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
    
    context = {
        'movie': movie,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'movies/movie_detail.html', context)


@login_required
def add_review(request, movie_id):
    """
    Add or edit review for a movie
    """
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Check if user already has a review
    existing_review = Review.objects.filter(
        movie=movie, 
        user=request.user
    ).first()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=existing_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            
            if existing_review:
                messages.success(request, 'Your review has been updated!')
            else:
                messages.success(request, 'Your review has been added!')
            
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm(instance=existing_review)
    
    context = {
        'form': form,
        'movie': movie,
        'editing': existing_review is not None
    }
    return render(request, 'movies/add_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    Delete user's own review
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    movie_id = review.movie.id
    review.delete()
    messages.success(request, 'Your review has been deleted.')
    return redirect('movie_detail', movie_id=movie_id)


def top_rated(request):
    """
    Show top rated movies
    """
    movies = Movie.objects.all()
    
    # Sort by average rating
    movies_with_ratings = [
        {
            'movie': movie,
            'avg_rating': movie.average_rating,
            'review_count': movie.review_count
        }
        for movie in movies if movie.review_count > 0
    ]
    
    # Sort by average rating (descending)
    movies_with_ratings.sort(key=lambda x: x['avg_rating'], reverse=True)
    
    context = {
        'movies_with_ratings': movies_with_ratings[:20]  # Top 20
    }
    return render(request, 'movies/top_rated.html', context)


def search_movies(request):
    """
    Search movies by title or director
    """
    query = request.GET.get('q', '')
    movies = Movie.objects.none()
    
    if query:
        movies = Movie.objects.filter(
            title__icontains=query
        ) | Movie.objects.filter(
            director__icontains=query
        )
    
    context = {
        'movies': movies,
        'query': query
    }
    return render(request, 'movies/search_results.html', context)
