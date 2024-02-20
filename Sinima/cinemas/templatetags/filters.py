from django import template
from cinemas import models

register = template.Library()


@register.inclusion_tag('filters_tags/cinema_filter.html')
def get_sessions_filter():
    return {'cinemas': models.Cinema.objects.all()}
