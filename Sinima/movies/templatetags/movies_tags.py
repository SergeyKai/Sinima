from django import template
from movies import models

register = template.Library()


@register.simple_tag()
def get_movies():
    return models.Movie.objects.all()


@register.inclusion_tag('movies/tags/movies_list_tag.html')
def get_movis_list_html():
    return {'movies': models.Movie.objects.all()}
