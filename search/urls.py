#-*- coding: utf-8 -*-
__author__ = 'Евгений'

from django.conf.urls import *

urlpatterns = patterns('search.views',
                        url(r'^search_movies/$','search_favorite', {'template_name': 'search/search.html'}, 'search_movies'),
                        url(r'^find_movie/$','search', {'template_name': 'search/search_result.html'}, 'search'),
)