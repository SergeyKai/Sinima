from django.shortcuts import render, get_object_or_404

from . import models


def movies_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movies/movies_list.html', context={'movies': movies})
    # return render(request, 'movies/movies_list.html', context={'movies': movies})


def movie_detail(request, movie_slug):
    movie = get_object_or_404(models.Movie, slug=movie_slug)

    ctx = {
        'title': movie.title,
        'description': movie.description,
        'release_date': movie.release_date,
        'poster': movie.poster,
        'actors': movie.actors.all(),
        'slug': movie.slug,
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
