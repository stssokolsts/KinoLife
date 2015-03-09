#-*- coding: utf-8 -*-
from django.db import models
import datetime
import requests
import vk
import re
import urllib2, urlparse
from KinoLife.settings import STATICFILES_DIRS


class Person(models.Model):
    person_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=150)
    photo = models.URLField()

    def __unicode__(self):
        return unicode(self.name)

    def from_dict(self, dct):
        """ Информация о персоне из словаря, возвращаемого API."""
        self.person_id = dct.get('id') or dct.get('attrib').get('id')
        self.name = dct.get('name') or dct.get('value')
        self.photo = dct.get('url','photo')
        self.save()


class Country(models.Model):
    """Страна производительница фильма"""
    name = models.CharField(max_length=30)

    def from_dict(self, name):
        self.name = name
        self.save()

    def __unicode__(self):
        return unicode(self.name)


class Genre(models.Model):
    """Жанр фильмов"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.name)

    def from_dict(self, name):
        self.name = name
        self.save()


class MovieBase(models.Model):
    """Базовый класс фильмов"""

    REMOVE = 1
    SHOW_FUTURE = 2
    FAVORITE = 3
    TOGETHER = 4

    STATE_CHOICE = (
        (REMOVE, 'Просмотрено') ,
        (SHOW_FUTURE, 'Надо посмотреть'),
        (FAVORITE, 'Избранное'),
        (TOGETHER, 'Посмотреть вместе'))


    movie_id = models.IntegerField(unique=True)  #+
    title = models.CharField(max_length=120)     #+
    year = models.IntegerField()                #
    type = models.CharField(max_length=30)       #+
    description = models.TextField()             #+
    poster = models.ImageField(upload_to="static/img")                 #
    trailer = models.URLField()                  #+
    title_russian = models.CharField(max_length=120)  #+
    title_original = models.CharField(max_length=120) #+
    url = models.URLField()                      #+
    rating_k = models.FloatField()             #+
    director = models.ManyToManyField(Person, related_name='director_movie')    #+
    cast = models.ManyToManyField(Person, related_name='cast_movie', null=True)        #+
    genre = models.ManyToManyField(Genre, null=True)        #
    country = models.ManyToManyField(Country, null=True)    #+
    runtime = models.IntegerField()
    votes_k = models.IntegerField()
    state = models.CharField(max_length=30, choices=STATE_CHOICE, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.title_russian)


    @models.permalink
    def get_absolute_url(self):
        return ('show_movie', (), { 'movie_id': self.movie_id })


    def from_dict(self, dct):
        """ Получить информацию о фильме из словаря, возвращаемого API."""
        self.year = int(dct.get('year'))
        self.type = dct.get('type')
        d = dct.get('description', '')
        self.description = re.sub("смотрите на Cinemate.cc", "", d)
        self.trailer = dct.get('trailer','')
        self.movie_id = int(dct['url'].split('/')[-2])
        self.title_original = dct.get('title_original', '')
        self.title_russian = dct.get('title_russian', '')
        self.title = self.title_russian
        self.rating_k = dct.get('kinopoisk', {}).get('rating',0)
        self.votes_k = dct.get('kinopoisk', {}).get('votes',0)
        self.runtime = dct.get('runtime', 0)
        if (self.type== "movie"):
            self.url = vk.search(self.title_russian, self.runtime, str(self.year))
        else:
            self.url = ""
        img = dct.get('poster', {}).get('big',{}).get('url', '')

        if img:
            p = requests.get(img)
            path = 'static\img\posters\\' + str(self.movie_id)  + '.jpg'
            #path = '/home/sokolenysh/KinoLife/static/img/posters/' + str(self.movie_id)  + '.jpg'
            out = open(path, "wb")
            out.write(p.content)
            out.close()
            path = 'img\posters\\' + str(self.movie_id)  + '.jpg'
            self.poster = path
        self.save()

        country = dct.get('country',{}).get('name', []) #????
        if (isinstance(country,unicode)):
            country = [country,]
        for c in country:
            try:
                old_c = Country.objects.get(name__exact = c)
                self.country.add(old_c)
            except Country.DoesNotExist:
                new_c = Country()
                new_c.from_dict(c)
                self.country.add(new_c)

        genre = dct.get('genre',{}).get('name', [])
        if isinstance(genre,unicode):
            genre = [genre, ]
        for g in genre:
            try:
                old_g = Genre.objects.get(name__exact=g)
                self.genre.add(old_g)
            except Genre.DoesNotExist:
                new_g = Genre()
                new_g.from_dict(g)
                self.genre.add(new_g)

        director = dct.get('director', {}).get('person', [])
        if isinstance(director, dict):
            director = [director,]
        for d in director:
            try:
                new_d = Person.objects.get(person_id__exact=d['id'])
                self.director.add(new_d)
            except Person.DoesNotExist:
                p = Person()
                p.from_dict(d)
                self.director.add(p)

        cast = dct.get('cast', {}).get('person', [])
        if isinstance(cast, dict):
            cast = [cast, ]
        for c in cast:
            try:
                p = Person.objects.get(person_id__exact=c['id'])
                self.cast.add(p)
            except Person.DoesNotExist:
                p = Person()
                p.from_dict(c)
                #self.save()
                self.cast.add(p)

# Create your models here.
