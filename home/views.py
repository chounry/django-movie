from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect, QueryDict
from .models import Movie, Episode
from .form import MovieForm
from django.db.models import Q
from itertools import chain
import re
# Create your views here.

def home(request):
    query = Movie.objects.all().exclude(film_type='tv')
    popular = query.order_by('rate_aver')[:12]
    tv = Episode.objects.all()[:12]
    context = {'latest':query[:12],
                'popular':popular,
                'tv':tv
    }
    return render(request, 'home.html', context)

def movies(request):
    query_movie = Movie.objects.all().exclude(film_type='tv')
    query_tv = Episode.objects.all()
    query = chain(query_tv,query_movie)

    return render(request, 'movies.html',context={'films':query})

def film_detail(request, slug):
    movie = None
    try:
        instance = Movie.objects.get(slug=slug)
    except ObjectDoesNotExistr:
        instance = Episode.objects.get(slug=slug)
        movie = instance.movie
        relate_ep = movie.episode_set.all()
    except:
        return render(request, 'warning.html')

    if(movie != None): # if it it the tv-serie we take it's related episode
        return render(request, 'movie-detail.html',context={'instance':instance,'relate_ep':relate_ep})

    return render(request, 'movie-detail.html',{'instance':instance})

def add_movie(request):

    movie_form = MovieForm(request.POST or None,request.FILES)
    if movie_form.is_valid():
        obj = movie_form.save(commit=False)
        obj.save()
        movie_form.save_m2m()
        return redirect(obj)

    return render(request,'movie_form.html',{'form':movie_form})

def filter(request, film_type, reso, genre, country, release):
    from_user = [film_type, reso, genre, country, release]
    from_user = list(map(lambda x: x.split('-'), from_user))

    for lis in from_user:
        if 'all' in lis:
            if len(lis) == 1:
                lis.clear()
            else:
                lis.remove('all')

    # change 'release' to integer
    from_user[-1] = list(map(lambda x: int(x), from_user[-1]))

    movies = Movie.objects.filter(
            Q(film_type__in=from_user[0]) |
            Q(reso__in=from_user[1]) |
            Q(genre__name__in=from_user[2]) |
            Q(country__in=from_user[3]) |
            Q(release__in=from_user[4])
        ).distinct()

    if(len(movies) == 0): # if no filter was chosen
        movies = Movie.objects.all()

    # get the episode for the film
    mov_list = list(movies)
    for m in movies:
        if m.episode_set.all():
            tem = list(m.episode_set.all())
            mov_list.remove(m)
            mov_list += tem

    return render(request, 'movies.html',{'films':mov_list})
