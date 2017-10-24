from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [

    # /
    url(r'^$',views.home, name = 'home'),

    # /movies/
    url(r'^movies/$',views.movies, name = 'movies'),
    
    # /movie/slug/
    url(r'movie/(?P<slug>[-\w]+)/$', views.movie_detail, name = 'movie_detail'),
   
    # /movie/add-movie/
    url(r'add-movie/$', views.add_movie, name = 'add_movie' ),

    # /add-rate/
    url(r'^add-rate/$', views.add_rate, name = 'add-rate')


	
]