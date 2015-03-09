# -*- coding: utf-8 -*-
__author__ = 'Евгений'

from django import template
from movie import movie
register = template.Library()

@register.inclusion_tag("tags/count_movie.html")
def count_movie(i):
    """возвращает количество фильмов данной категории"""
    return {'count': movie.count_movie(int(i))}
