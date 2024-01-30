from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


# admin.site.register(models.Actor)

@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthdate', 'get_phot')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'birthdate')

    prepopulated_fields = {'slug': ('name',)}

    fields = ('name', 'birthdate', 'photo', 'get_phot', 'slug')
    readonly_fields = ('get_phot',)

    def get_phot(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" height="100px"/>')


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date', 'get_poster')
    list_display_links = ('id', 'title')
    list_filter = ('release_date', 'title')
    prepopulated_fields = {'slug': ('title',)}

    fields = ('title', 'release_date', 'poster', 'get_poster', 'description', 'actors', 'slug')
    readonly_fields = ('get_poster',)

    def get_actors(self, obj):
        ac_names = [a.name for a in obj.actors.all()]
        return f'\n'.join(ac_names)

    def get_poster(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" height="100px" />')

    get_poster.short_description = 'Постер'

# admin.site.register(models.Movie, MovieAdmin)
