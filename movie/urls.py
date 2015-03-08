#-*- coding: utf-8 -*-
__author__ = 'Евгений'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('movie.views',
                       url(r'^$', 'index', { 'template_name' : 'movie/index.html'}, name='movies_home'),
                       url(r'^movie/(?P<movie_id>[-\d]+)/$', 'show_movie', {'template_name':'movie/movie.html'},
                           'show_movie'),
                       url(r'^movies/(?P<movies_slug>[-\d]+)/$', 'movies', {'template_name' : 'movie/movies.html'},
                           'show_movies'),
                       url(r'^movies/$', 'all_movies', {'template_name':'movie/all_movies.html'},
                           'show_all_movies'),

)