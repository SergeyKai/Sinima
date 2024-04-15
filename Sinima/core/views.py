from django.core.mail import send_mass_mail
from django.shortcuts import render, redirect

from movies import models

from django.conf import settings


def home(request):
    movies = models.Movie.objects.all()
    ctx = {
        'movies': movies,
    }

    return render(request, 'core/home.html', context=ctx)


def about(request):
    return render(request, 'core/about.html')


def forbidden(request):
    return render(request, 'core/forbidden.html')
