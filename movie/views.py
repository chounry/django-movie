from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Movies

# Create your views here.

def Home():
    template = 'home.html'
    movies = Movies.objects.all()
    rate_range = movies.order_by('')
    latest = movies[:5]
    most_rate = []
    most_commented = []




def genre(request):
    context = {
        'genre':[ 'Romance','Action',
                'Ski-Fi','Horror','Family','Crime',
                'War','Drama','Adventure','Animation'
                 ]
    }
    return render(request, 'genre.html', context)

def genreDetail(request,genre_type):
    genre_type = genre_type
    if genre_type == 'SkiFi':
        genre_type = 'Ski-Fi'

    movies = Movies.objects.all()
    show_movies = []

    for movie in movies:
        if genre_type in movie.genre:
            show_movies.append(movie)


    context = {'show_movies':show_movies,}
    return render(request, 'genre-detail.html', context)









