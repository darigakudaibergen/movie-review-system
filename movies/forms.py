
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['rating', 'title', 'comment']
        widgets = {
            'rating': forms.Select(
                choices=[(i, f'{i} ★') for i in range(1, 6)],
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Give your review a title'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Write your review here...'
                }
            ),
        }
        labels = {
            'rating': 'Your Rating',
            'title': 'Review Title',
            'comment': 'Your Review'
        }
