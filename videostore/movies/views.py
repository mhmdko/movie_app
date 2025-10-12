from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.order_by("movie_title")
    return render(request, "movies/movie_list.html", {"movies": movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movies/movie_detail.html", {"movie": movie})

def movie_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_list")
    else:
        form = MovieForm()
    return render(request, "movies/movie_form.html", {"form": form, "mode": "Create"})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_detail", pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, "movies/movie_form.html", {"form": form, "mode": "Update"})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movies:movie_list")
    return render(request, "movies/movie_confirm_delete.html", {"movie": movie})

