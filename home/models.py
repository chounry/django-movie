from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase
from genre.models import Genre

import re
# Create your models here.

class Movie(models.Model):
    resolution = (
        ('hd','HD'),
        ('sd','SD'),
        ('cam','CAM'),
    )
    film_type = models.CharField(max_length=10,null=True, choices=(('movie','Movie'),('tv','Tv Series')))
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, editable=False)
    reso = models.CharField('Resolustion', max_length=3, choices=resolution)
    release = models.IntegerField('Release Year')
    upload_date = models.DateField(auto_now=True)
    caption = models.TextField(max_length=1000, null=True, blank=True)
    video = models.FileField(blank=True, null=True)
    img = models.FileField('Image')
    rate_aver = models.DecimalField(max_digits=3,decimal_places=1,default=0.0,editable=False)
    number_rater = models.PositiveSmallIntegerField(default=0,editable=False)
    language = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)

    def get_absolute_url(self):
        return reverse('movie:film_detail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title + ' - ' + self.film_type

    class Meta:
        ordering = ['-upload_date']

class Episode(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    video = models.FileField()
    slug = models.SlugField(unique=True,blank=True)
    epi_num = models.IntegerField('Episode number')
    season_num = models.PositiveSmallIntegerField('Season number')
    title = models.CharField(max_length=50,blank=True,editable=False)

    def get_absolute_url(self):
        return reverse('movie:film_detail', kwargs={'slug':self.slug})

    def save(self):
        self.title = self.movie.title + ' - ' + 'Season ' + str(self.season_num)
        self.slug = slugify(self.movie.title + ' ' + str(self.epi_num))
        super(Episode, self).save()

    def __str__(self):
        return self.movie.title +' - ' + str(self.epi_number)

def create_movie_slug(instance):
    i = 1
    while True:
        new_slug = slugify(instance.title) + '-' +str(i)
        slug = Movie.objects.filter(slug = new_slug)
        if not slug:
            break
        i+=1

    return new_slug

def pre_save_movie_receiver(sender, instance, *arg, **kwarg):
    if not instance.slug:
        instance.slug = create_movie_slug(instance)

pre_save.connect(pre_save_movie_receiver, sender=Movie)
