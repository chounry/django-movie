from django.conf.urls import url
from . import views

app_name = 'rate'

urlpatterns = [
    # /add-rate/
    url(r'^$', views.add_rate, name = 'add-rate'),
]
