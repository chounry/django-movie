from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Movies(models.Model):
    resolution = (
        ('HD','HD'),
        ('DVD','DVD'),
        ('CAM','CAM'),
    )
    title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 500, help_text = "e.g Romance , Action , ...")
    reso = models.CharField('Resolustion' ,max_length = 3,choices = resolution)
    release = models.CharField(max_length = 4)
    upload_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    file = models.CharField(max_length = 200)
    img = models.CharField('Image',max_length = 200)                                                            
    comment_count = models.CharField(editable = False, max_length = 5)
    rate_count  = models.CharField(editable = False, max_length = 1)

    def __str__(self):
        return self.title






