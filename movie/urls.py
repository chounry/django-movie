from django.conf.urls import url
from . import views


urlpatterns = [

    # /
    url(r'^$',views.Home, name = 'home'),

    # /genre/
    url(r'^genre/$', views.genre, name = 'genre'),

    # /genre/eg.Romance/
    url(r'^genre/(?P<genre_type>[a-zA-Z]+)/$', views.genreDetail, name = 'genre-detail'),
]