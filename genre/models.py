from django.db import models
from django.utils.text import slugify

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.title

    def save(self):

        self.slug = slugify(self.title)
        super(Genre,self).save()
