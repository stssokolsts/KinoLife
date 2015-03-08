# -*- coding: utf-8 -*-
__author__ = 'Евгений'
import requests
from models import MovieBase

APIKEY = '198c65f8632903e86b10bfe8d936c2d7aa4a0560'

URL = 'http://api.cinemate.cc/'

TYPE_URl = ['movie', 'movie.list', 'movie.search', 'person', 'person.movies', 'person.search']

FORMAT = 'json'

#movie = ['movie', 'movie.list', 'movie.search']

#person = ['person', 'person.movies', 'person.search']

def set_movie_from_json (dct):
    movie_id = int(dct['url'].split('/')[-2])


#доработай
def get_movie_by_id(id):
    """ поиск фильма по id на cinemate, вернет сорвать с фильмом или None, если не найден """
    try:
        req = requests.get(URL+TYPE_URl[0], params = {'apikey': APIKEY, 'id' : id, 'format': FORMAT})
        if (req.status_code == requests.codes.ok and not req.json().get('error')):
            print(req.json())
            return req.json()['movie'][0]
        else:
            return None
    except requests.RequestException:
        return None



def format_str (list):
    s = ""
    for l in list:
        s += l.name + ", "
    s = s[:-2]
    return s


def search(q):
    """поиск фильма по заголовку, вернёт список совпадений"""
    try:
        req = requests.get(URL+TYPE_URl[2], params = {'apikey': APIKEY, 'term' : str(q), 'format': FORMAT})
        if (req.status_code == requests.codes.ok and not req.json().get('error')):
            print(req.json())
            print(len(req.json()['movie']))
            return req.json()['movie']
        else:
            return []
    except requests.RequestException:
        return []

def search_favorite():
    type = 'movie'
    year = 2006
    genre = 'romance'
    date_from = '01.01.2003'
    date_to = '01.01.2001'
    page = 1
    per_page = 20
    try:
        req = requests.get(URL+TYPE_URl[1],
                           params = {'apikey': APIKEY,
                                     'type' : type,
                                     'format': FORMAT,
                                     'per_page' : per_page,
                                     'genre' : genre,
                                     'page': '100',
                                     'year' : year})
        print("r")
        print(req)
        if (req.status_code == requests.codes.ok):
            if (not req.json().get('error')):
                print(req.json())
                print(req.json().get('movie'))
                print(len(req.json().get('movie')))
        else:
            return []
    except requests.RequestException:
        return []


def copy_base():
    print('p')
    s = 0
    l_temp = []
    list_res = []
    type = 'movie'
    year = 2008
    genre = 'romance'
    #date_from = '01.01.2003'
    date_to = '01.01.2001'
    page = 0
    per_page = 20
    list_movie = []
    p = {'apikey': APIKEY,
         'type' : type,
         'format': FORMAT,
         'per_page' : per_page,
         'genre' : genre,
         'page': page,
         'year' : year}
    try:
        req = requests.get(URL+TYPE_URl[1],
                           params = p)
        print(req.json())
        if (req.status_code == requests.codes.ok):
            if (not req.json().get('error')):
                print("l1")
                l_temp = req.json().get('movie', [])
                print(l_temp)
                for l in l_temp:
                    print(l)
                    print("l")
                    if isinstance(l,dict):
                        movie_id = l.get('id', 0)
                        try:
                            movie = MovieBase.objects.get(movie_id__exact= movie_id)

                        except MovieBase.DoesNotExist:
                            movie_dct = get_movie_by_id(movie_id)
                            if (movie_dct):
                                movie = MovieBase()
                                movie.from_dict(dct = movie_dct)
                                s+=1
                                print("фильмов де-факто - " + str(s))
                            else:
                                movie = None
                            list_movie.append(l.get('id', 0))
                print(l_temp)
    except requests.RequestException:
        return list_movie
    while not (l_temp == []):
        try:
            page+=1
            p.update({'page' : page})
            req = requests.get(URL+TYPE_URl[1],
                               params = p)
            if (req.status_code == requests.codes.ok):
                if (not req.json().get('error')):
                    print("other")
                    print("page:")
                    print(page)
                    l_temp = req.json().get('movie', [])
                    for l in l_temp:
                        if isinstance(l,dict):
                            movie_id = l.get('id', 0)
                            try:
                                movie = MovieBase.objects.get(movie_id__exact= movie_id)
                            except MovieBase.DoesNotExist:
                                movie_dct = get_movie_by_id(movie_id)
                                if (movie_dct):
                                    movie = MovieBase()
                                    movie.from_dict(dct = movie_dct)
                                    s+=1
                                    print("фильмов де-факто - " + str(s))
                                else:
                                    movie = None
                                list_movie.append(l.get('id', 0))
                    print(l_temp)
            else:
                return list_movie
        except requests.RequestException:
            return list_movie
    print(list_movie)
    print(len(list_movie))


def copy_base_count():
    print('p')
    s = 0
    l_temp = []
    list_res = []
    type = 'movie'
    year = 2008
    genre = 'romance'
    #date_from = '01.01.2003'
    date_to = '01.01.2001'
    page = 0
    per_page = 20
    list_movie = []
    p = {'apikey': APIKEY,
         'type' : type,
         'format': FORMAT,
         'per_page' : per_page,
         'genre' : genre,
         'page': page,
         'year' : year}
    try:
        req = requests.get(URL+TYPE_URl[1],
                           params = p)
        print(req.json())
        if (req.status_code == requests.codes.ok):
            if (not req.json().get('error')):
                print("l1")
                l_temp = req.json().get('movie', [])
                print(l_temp)
                for l in l_temp:
                    print(l)
                    print("l")
                    if isinstance(l,dict):
                        list_movie.append(l.get('id', 0))
                print(l_temp)
    except requests.RequestException:
        return list_movie
    while not (l_temp == []):
        try:
            page+=1
            p.update({'page' : page})
            req = requests.get(URL+TYPE_URl[1],
                               params = p)
            if (req.status_code == requests.codes.ok):
                if (not req.json().get('error')):
                    print("other")
                    print("page:")
                    print(page)
                    l_temp = req.json().get('movie', [])
                    for l in l_temp:
                        if isinstance(l,dict):
                            list_movie.append(l.get('id', 0))
                    print(l_temp)
            else:
                return list_movie
        except requests.RequestException:
            return list_movie
    print(list_movie)
    print(len(list_movie))