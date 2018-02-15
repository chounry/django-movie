from django.db import models
from django.contrib.auth.models import User
from home.models import Movie

# Create your models here.
class Rate(models.Model):
    value = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
