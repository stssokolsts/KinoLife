# -*- coding: utf-8 -*-
__author__ = 'Евгений'
from models import MovieBase


def count_movie(id):
    return int(MovieBase.objects.filter(state__exact = int(id)).count())
