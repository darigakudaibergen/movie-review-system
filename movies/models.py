from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2030)]
    )
    director = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        related_name='movies'
    )
    poster_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return 0

    @property
    def review_count(self):
        return self.reviews.count()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.rating}★)"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        unique_together = ['movie', 'user']