from django import template
from movies import models

register = template.Library()


@register.simple_tag()
def get_movies():
    return models.Movie.objects.all()


@register.inclusion_tag('tickets/tickets_tags/ticket_form_wrapper.html')
def get_purchase_ticket_form():
    return {'movies': models.Movie.objects.all()}
