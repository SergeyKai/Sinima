from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404

from cinemas.models import Session
from . import models


def movies_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movies/movies_list.html', context={'movies': movies})
    # return render(request, 'movies/movies_list.html', context={'movies': movies})


def get_movi_session(request, movie):
    sessions = Session.objects.filter(movie=movie)
    if request.GET.get('cinema'):
        sessions = sessions.filter(room__cinema=request.GET.get('cinema'))
    if request.GET.get('date'):
        selected_date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d').date()
        next_day = selected_date + timedelta(days=1)

        sessions = sessions.filter(start_time__gte=selected_date, start_time__lt=next_day)

    return sessions


# http://127.0.0.1:8000/movies/master-i-margarita/?cinema=2&date=

def movie_detail(request, movie_slug):
    movie = get_object_or_404(models.Movie, slug=movie_slug)

    ctx = {
        'title': movie.title,
        'description': movie.description,
        'release_date': movie.release_date,
        'poster': movie.poster,
        'actors': movie.actors.all(),
        'slug': movie.slug,
        'sessions': get_movi_session(request, movie),
        'movie': movie,
    }

    return render(request, 'movies/movie_detail.html', context=ctx)


def actor_detail(request, actor_slug):
    actor = get_object_or_404(models.Actor, slug=actor_slug)

    ctx = {
        'name': actor.name,
        'birthdate': actor.birthdate,
        'photo': actor.photo,
        'slug': actor.slug,
    }

    return render(request, 'movies/actor_detail.html', context=ctx)
