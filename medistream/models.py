from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)


class Speciality(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Specialities'
        ordering = ('name',)


class CustomUser(AbstractUser):
    speciality = models.ForeignKey(Speciality, blank=True, null=True, related_name='specialities')

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ('username',)


class Organizer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Organizers'
        ordering = ('name',)


class EventType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Event types'
        ordering = ('name',)


class Event(models.Model):
    ''' Model features for an event '''
    type = models.ForeignKey(EventType, related_name='events', blank=True, null=True)
    title = models.CharField(max_length=200)
    organizer = models.ForeignKey(Organizer, related_name='events')
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    abstract = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = 'Events'
        ordering = ('start_date', 'title',)


class Speaker(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Speakers'
        ordering = ('name',)


class Talk(models.Model):
    ''' Model features for a talk '''
    start_time = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=200)
    event = models.ForeignKey(Event, related_name='talks')
    speaker = models.ForeignKey(Speaker, related_name='talks', blank=True, null=True)
    abstract = models.TextField(blank=True)
    pod_id = models.IntegerField(blank=True, null=True)
    pod_preview_id = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name_plural = 'Talks'
        unique_together = ('event', 'start_time')
        ordering = ('start_time',)
