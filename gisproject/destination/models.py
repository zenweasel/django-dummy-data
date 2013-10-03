from django.db import models


class City(models.Model):
    str_slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    destinations = models.ManyToManyField('Destination', through='DestinationCity')

    def __unicode__(self):
        return u'%s' % self.name


class DestinationCity(models.Model):
    city = models.ForeignKey(City)
    destination = models.ForeignKey('Destination')


class Destination(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2, null=True, blank=True)

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % self.name