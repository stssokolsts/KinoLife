# -*- coding: utf-8 -*-
__author__ = 'Евгений'
from movie.models import MovieBase
from movie.cinemate import get_movie_by_id
from movie.models import Genre


def set_search_movie():
    rating_min = 5
    votes_min = 300
    res = MovieBase.objects.filter(genre__name__exact = 'мелодрама')\
        .filter(genre__name__exact = 'комедия')\
        .filter(rating_k__gt = rating_min)\
        .exclude(state__exact = MovieBase.REMOVE)\
        .filter(votes_k__gt = votes_min).order_by('?')[:12]
    return res

def search_by_name(list_movie):
    list_rez = []
    if (len(list_movie)>5):
        list_movie = list_movie[:5]
    for l in list_movie:
        if isinstance(l,dict):
            id = l.get('id', '')
            print("id:")
            print(id)
            m = get_movie_by_id(l.get('id', ''))
            print("элемент по айди:")
            print(m)

            if m:
                try:
                    print("old^")
                    list_rez.append(MovieBase.objects.get(movie_id__exact = id))
                    print(list_rez)
                except MovieBase.DoesNotExist:
                    movie_dct = get_movie_by_id(id)
                    if (movie_dct):
                        mov = MovieBase()
                        mov.from_dict(dct = movie_dct)
                        list_rez.append(mov)
                        print("new")
                        print("list:")
                        print(list_rez)
                    else:
                        mov = None
    return list_rez


