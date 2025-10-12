from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "movie_id",
            "movie_title",
            "actor1_name",
            "actor2_name",
            "director_name",
            "movie_genre",
            "release_year",
        ]
