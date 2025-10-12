from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

GENRE_CHOICES = [
    ("Comedy", "Comedy"),
    ("Romance", "Romance"),
    ("Action", "Action"),
    ("Drama", "Drama"),
    ("Horror", "Horror"),
    ("Sci-Fi", "Sci-Fi"),
]

class Movie(models.Model):
    movie_id = models.PositiveIntegerField(primary_key=True, verbose_name="MovieID")
    movie_title = models.CharField(max_length=200, verbose_name="MovieTitle")
    actor1_name = models.CharField(max_length=120, verbose_name="Actor1Name")
    actor2_name = models.CharField(max_length=120, blank=True, verbose_name="Actor2Name")
    director_name = models.CharField(max_length=120, verbose_name="DirectorName")
    movie_genre = models.CharField(max_length=20, choices=GENRE_CHOICES, verbose_name="MovieGenre")
    release_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.date.today().year + 1),
        ],
        verbose_name="ReleaseYear",
    )

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"

