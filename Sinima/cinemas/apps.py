from django.apps import AppConfig


class CinemasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cinemas'
    verbose_name = 'Кинотеатры'

    def ready(self):
        from .models import Room, Seat
        from .signals import generate_room_seats
