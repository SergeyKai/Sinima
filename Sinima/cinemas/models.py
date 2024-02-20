from django.db import models

from movies.models import Movie


class Cinema(models.Model):
    """ Информация о кинотеатрах """
    name = models.CharField(max_length=255, verbose_name='Название')
    address = models.TextField(verbose_name='Адрес')
    map_link = models.CharField(max_length=255, null=True)
    logo = models.ImageField(upload_to='cinema', default='cinema/film-reel.png')

    def __str__(self):
        return f'Кинотеатр: {self.name} адрес: {self.address} id: {self.pk}'

    class Meta:
        verbose_name = 'Кинотеатр'
        verbose_name_plural = 'Кинотеатры'


class Room(models.Model):
    """ Информация о зале кинотеатра """
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Кинотеатр')
    name = models.CharField(max_length=50, verbose_name='Наименование зала')
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')

    def __str__(self):
        return f'Зал: {self.name} кинотеатр: {self.cinema} вместимость: {self.capacity} id: {self.pk}'

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Seat(models.Model):
    """ Место """
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Зал')
    row = models.PositiveIntegerField(verbose_name='Ряд')
    number = models.PositiveIntegerField(verbose_name='место №')

    def __str__(self):
        return f'Место: Зал: {self.room.name} Ряд: {self.row} Место: {self.number}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Session(models.Model):
    """ Информация о сеансе  """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Зал')
    start_time = models.DateTimeField(verbose_name='Дата показа')
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена билета')

    def __str__(self):
        return f'Показ: фильм: {self.movie} зал: {self.room} начало: {self.start_time} цена: {self.ticket_price} id: {self.pk}'

    class Meta:
        verbose_name = 'Показ'
        verbose_name_plural = 'Показы'
