from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def admin_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Вы не авторизованы')
        elif not request.user.is_superuser:
            return redirect('forbidden')
        else:
            return func(request, *args, **kwargs)

    return wrapper
