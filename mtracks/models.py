from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_ratings(value):
    if value < 1 or value > 5:
        raise ValidationError(
            _('not a proper Rating please pass a value in between 1-5'),
            params={'value':value},
            )



class Genres(models.Model):
    genres_name = models.CharField(max_length=200, editable=True, help_text="Name of the genres",unique=True)
    def __str__(self):
        return self.genres_name


class Track(models.Model):
    genres = models.ForeignKey(Genres,help_text="Genres the title belongs to")
    track_name = models.CharField(max_length=200,editable=True,null=False,blank=False,help_text="Name of the Track")
    rating = models.IntegerField(default=0,validators=[validate_ratings])
    def __str__(self):
        return '%s %s %s %s' % (self.track_name," [",self.genres,"] ")





