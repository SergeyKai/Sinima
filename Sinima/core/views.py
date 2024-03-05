from django.core.mail import send_mass_mail
from django.shortcuts import render, redirect

from core.forms import FeedBackForm
from movies import models

from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            u_email = form.cleaned_data.get('email')
            print(u_email)
            msg = ('Hello!',
                   'Test Mail',
                   settings.DEFAULT_FROM_EMAIL,
                   [u_email])
            send_mass_mail((msg,))
            return redirect('list_session')

    movies = models.Movie.objects.all()
    form = FeedBackForm
    ctx = {
        'movies': movies,
        'form': form
    }

    return render(request, 'core/home.html', context=ctx)


def about(request):
    return render(request, 'core/about.html')


def forbidden(request):
    return render(request, 'core/forbidden.html')
