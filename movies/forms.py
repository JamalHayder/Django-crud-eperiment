from django import forms
from .models import Movie, Cast, Trivia


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['director', 'movie_title', 'genre', 'movie_art']


class CastForm(forms.ModelForm):

    class Meta:
        model = Cast
        fields = ['role', 'cast_name']


class TriviaForm(forms.ModelForm):

    class Meta:
        model = Trivia
        fields = ['trivia_details']
