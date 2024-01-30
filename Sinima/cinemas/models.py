from django.db import models

from movies.models import Movie


class Cinema(models.Model):
    """ Информация о кинотеатрах """
    name = models.CharField(max_length=255)
    address = models.TextField()


class Room(models.Model):
    """ Информация о зале кинотеатра """
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()


class Session(models.Model):
    """ Информация о сеансе  """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
