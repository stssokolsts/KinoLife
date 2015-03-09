# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from movie import cinemate
from search import search_by_name,set_search_movie


def search(request, template_name="movie/search_result.html"):
    q = request.GET.get('q', '')
    #cinemate.search(q.encode('utf-8'))
    movies = search_by_name(cinemate.search(q.encode('utf-8')))
    page_title = "Результаты поиска по запросу '"+q.encode('utf-8')+"'"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def search_favorite(request, template_name="movie/search.html"):
    """рандомные фильмы по опредленным фильтрам"""
    movies = set_search_movie()
    page_title = "Поиск фильмов"
    #cinemate.search_favorite()
    #cinemate.copy_base()
    #cinemate.copy_base_count()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
# Create your views here.
