from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models

admin.site.register(models.Seat)


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'get_movie_poster', 'room', 'start_time', 'ticket_price')
    list_display_links = ('id', 'movie')
    list_filter = ('movie', 'room', 'start_time', 'ticket_price')

    def get_movie_poster(self, obj):
        return mark_safe(f'<img src="{obj.movie.poster.url}" height="100px"/>')


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cinema', 'capacity')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'cinema', 'capacity')


@admin.register(models.Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'address')
