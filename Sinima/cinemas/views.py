from django.shortcuts import render

from .models import Session


def list_session(request):
    sessions = Session.objects.all()

    return render(request, 'movies/list_session.html', {'sessions':sessions})
