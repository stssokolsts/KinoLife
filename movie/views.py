# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import MovieBase
import vk,cinemate, json

def index(request, template_name="movie/index.html"):
    #movie_dct = cinemate.get_movie_by_id(2116)
    #m = MovieBase()
    #if (movie_dct):
    #    m.from_dict(movie_dct)

    #print(movie_dct)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))



def show_movie(request, movie_id, template_name="movie/movie.html"):
    """представление для просмотра одного фильма"""
    if request.method == 'POST':
        if request.is_ajax():
            post_data = request.POST.copy()
            type_m = int(post_data.get("type", 0))
            response_dict = {}
            response_dict.update({'success': 'True'})
            try:
                movie = MovieBase.objects.get(movie_id__exact=movie_id)
                if (type_m == movie.REMOVE):
                    movie.state = movie.REMOVE
                elif (type_m == movie.SHOW_FUTURE ):
                    movie.state = movie.SHOW_FUTURE
                elif (type_m == movie.FAVORITE):
                    movie.state = movie.FAVORITE
                elif (type_m == movie.TOGETHER):
                    movie.state = movie.TOGETHER
                movie.save()
                response_dict.update({'success': 'True', 'type' : movie.state})
            except MovieBase.DoesNotExist:
                response_dict.update({'success': 'False'})
            return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
    try:
        movie = MovieBase.objects.get(movie_id__exact=movie_id)
    except MovieBase.DoesNotExist:
        movie_dct = cinemate.get_movie_by_id(movie_id)
        if (movie_dct):
            movie = MovieBase()
            movie.from_dict(dct = movie_dct)
        else:
            movie = None
    if (movie):
        page_title = movie.title_russian
        cast = cinemate.format_str(movie.cast.all())
        country = cinemate.format_str(movie.country.all())
        director = cinemate.format_str(movie.director.all())
        genre = cinemate.format_str(movie.genre.all())
        year = movie.year
        if not (movie.trailer == ""):
            youtube_url = vk.get_yt_url(movie.trailer)
        if (movie.type == "serial"):
            type = "Сериал"
    else:
        raise Http404
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def movies(request, movies_slug, template_name="movie/movies.html"):
    """просмотр категории фильмов"""
    movies = MovieBase.objects.filter(state__exact = movies_slug)
    try:
        movies_name_category = MovieBase.STATE_CHOICE[int(movies_slug) - 1][1]
        page_title = movies_name_category
        pass
    except IndexError:
        raise Http404
    if (movies_slug == "all"):
        movies = MovieBase.objects.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def all_movies(request, template_name="movie/movies.html"):
    print("12")
    movies_name_category = "Личная киноколлекция просто!"
    #movies = MovieBase.objects.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def about(request, template_name="movie/movies.html"):
    page_title = "О сайте "
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


# Create your views here.
