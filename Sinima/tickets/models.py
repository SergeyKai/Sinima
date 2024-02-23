from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.conf import settings

from cinemas.models import Seat, Session
from .qr_api import QR

User = get_user_model()


class Ticket(models.Model):
    """ Билет """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='Сеанс')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, verbose_name='Место')
    purchase_time = models.DateTimeField(auto_now_add=True, verbose_name='Время покупки')

    svg_qr_code = models.TextField(verbose_name='QR код')

    # checked = models.BooleanField(default=False, verbose_name='Проверен')

    def get_absolute_url(self):
        return reverse('check_ticket', kwargs={'ticket_id': self.pk})

    def set_qr(self):
        # print(type(QR(self.get_absolute_url()).generate_qr()))
        self.svg_qr_code = str(QR(f'{settings.DEFAULT_HOST}{self.get_absolute_url()}').generate_qr())
        self.save()

    def __str__(self):
        return f'Билет: Пользователь: {self.user} Место: {self.seat} Время покупки: {self.purchase_time} <id: {self.pk}>'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        ordering = ['session__start_time']
