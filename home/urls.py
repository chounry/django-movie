from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [

    # /
    url(r'^$',views.home, name = 'home'),

    # /movies/
    url(r'^film/$',views.movies, name = 'film'),

    # /movie/slug/
    url(r'film/(?P<slug>[-\w]+)/$', views.film_detail, name = 'film_detail'),

    # /movie/add-movie/
    url(r'add-movie/$', views.add_movie, name = 'add_movie' ),

    #(/filter/)
    url(r'filter/(?P<film_type>\w+)/(?P<reso>[\w-]+)/(?P<genre>[\w-]+)/(?P<country>[\w-]+)/(?P<release>[\d\w-]*)/$', views.filter, name = 'filter'),

]
