from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect

from .models import Movie
from .form import MovieForm

# Create your views here.

def home(request):
    return render(request,'home.html')


def movies(request):
    return render(request, 'movies.html')

def movie_detail(request, slug):
    try:
        instance = Movie.objects.get(slug=slug)
    except:
        return render(request, 'warning.html')
    return render(request, 'movie-detail.html',{'instance':instance})




    return render(request,'movie-detail.html')

def add_movie(request):
    
    movie_form = MovieForm(request.POST or None,request.FILES)

    if movie_form.is_valid():
        obj = movie_form.save(commit=False)
        obj.save()
        movie_form.save_m2m()
        return redirect(obj)


    return render(request,'movie_form.html',{'form':movie_form})




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


def add_rate(request):
    movie_id = request.GET.get('movie_id')
    rate = request.GET.get('rate')

    try:
        movie_id = int(movie_id)
        rate = int(rate)
    except: 
        return HttpResponse('ok')

    try:
        movie_obj = Movie.objects.get(id=movie_id)
    except:
        return HttpResponse('ok')

    if(rate >= 1 and rate >= 10):
        old_rate = movie_obj.rating
        number_rater = movie.number_rater
        reverse = old_rate * number_rater

        new_rate = (reverse + rate) / (number_rater + 1)

        movie_obj.number_rater += 1 # increament rater
        movie_obj.save()

    return HttpResponse('ok')







