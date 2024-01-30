from django.shortcuts import render

from movies import models


def home(request):
    movies = models.Movie.objects.all()
    return render(request, 'core/home.html', context={'movies': movies})


def about(request):
    return render(request, 'core/about.html')
