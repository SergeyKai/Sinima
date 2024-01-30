from django.db import models
from django.urls import reverse


class Actor(models.Model):
    """ Информация о актерах """
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='actor_photos/')

    def __str__(self):
        return f'Актер: {self.name} id: {self.pk}'

    def get_absolute_url(self):
        return reverse('actor', kwargs={'actor_slug': self.slug})

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Movie(models.Model):
    """ Информация о фильме """
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='movie_posters/')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return f'Актер: {self.title} id: {self.pk}'

    def get_absolute_url(self):
        return reverse('movie', kwargs={'movie_slug': self.slug})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-release_date', 'title']
