from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Room, Seat


@receiver(post_save, sender=Room)
def generate_room_seats(sender, instance, created, **kwargs):
    if created:
        seat_quantity = instance.capacity // instance.rows_quantity

        for row in range(1, instance.rows_quantity + 1):
            for seat in range(1, seat_quantity + 1):
                Seat.objects.create(
                    room=instance,
                    row=row,
                    number=seat,
                )

