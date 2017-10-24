from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase

import re
# Create your models here.
class Country(TagBase):

    # ... fields here

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    # ... methods (if any) here


class TaggedCountry(GenericTaggedItemBase):
    # TaggedWhatever can also extend TaggedItemBase or a combination of
    # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
    # allows using the same tag for different kinds of objects, in this
    # example Food and Drink.

    # Here is where you provide your custom Tag class.
    tag = models.ForeignKey(Country,
                            related_name="%(app_label)s_%(class)s_items")



class Movie(models.Model):
    resolution = (
        ('HD','HD'),
        ('DVD','DVD'),
        ('CAM','CAM'),
    )
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True,editable=False)
    reso = models.CharField('Resolustion' ,max_length=3,choices=resolution)
    release = models.IntegerField('Release Year')
    upload_date = models.DateField(auto_now=True,null=True)
    caption = models.CharField(max_length=1000, null=True, blank=True)
    video = models.FileField()
    img = models.FileField('Image')
    views = models.IntegerField(editable=False,null=True)
    rating = models.IntegerField(editable=False,null=True)
    number_rater = models.IntegerField(editable=False,null=True)

    genre = TaggableManager(verbose_name='Genre')
    country = TaggableManager(verbose_name='Country', through="TaggedCountry", blank=True)

    def get_absolute_url(self):
        return reverse('movie:movie_detail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title + " - " + str(self.id)

    class Meta:
        ordering = ['-upload_date']


def create_slug(instance):
    new_slug = slugify(instance.title)
    slug = Movie.objects.filter(slug = new_slug)
    slug_exist = slug.exists()
    if slug_exist:
        num = int(re.findall('(?<=-)\d+$',slug.first()))
        new_slug = '%s-%s'%(new_slug, num)

    return new_slug


def pre_save_movie_receiver(sender, instance, *arg, **kwarg):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_movie_receiver, sender=Movie)






