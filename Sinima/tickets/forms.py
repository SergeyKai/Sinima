from django import forms
from django.forms.widgets import CheckboxInput
from django.utils.html import mark_safe
from django.contrib.auth import get_user_model
from cinemas.models import Session
from .models import Ticket
from cinemas.models import Seat

from .qr_api import QR

User = get_user_model()


class SeatsCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    """ Видежет чекбокса для посадочных мест в зале """

    def __init__(self, booked_seats, session, *args, **kwargs):
        """ booked_seats: queryset забронированных посадочных мест """
        super().__init__(*args, **kwargs)
        self.booked_seats = booked_seats
        self.session = session

    def create_option(
            self,
            name,
            value,
            label,
            selected,
            index,
            subindex=None,
            attrs=None
    ):
        """ Установка атрибута 'disable' для чекбоксов забранированного посадочного места """
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        seat_price = self.session.ticket_price
        attrs.update({
            'data-price': seat_price,
            'class': 'seat'
        })
        if value in self.booked_seats:
            option['attrs']['disabled'] = True
        option['attrs']['title'] = label
        try:
            seat_number = label.split()[-1]
            row_number = label.split()[-3]
        except IndexError:
            seat_number = ''
            row_number = ''
            seat_price = ''

        option['label'] = mark_safe(
            f'<span class="checkbox" ></span><div class="seat_info"><span> Ряд: {row_number} </span><span> Место: {seat_number}</span><span class="seat_price"> Цена: {seat_price}</span></div>'
        )
        return option


class PurchaseTicketForm(forms.Form):
    """ Форма покупки билетов """
    seat = forms.ModelMultipleChoiceField(queryset=Seat.objects.all(), required=True)

    def __init__(self, session, *args, **kwargs):
        super(PurchaseTicketForm, self).__init__(*args, **kwargs)

        self.session = session

        self.booked_seats = Ticket.objects.values_list('seat', flat=True).filter(session=session)
        self.fields['seat'].widget = SeatsCheckboxSelectMultiple(self.booked_seats, session)

        seats = Seat.objects.filter(room=session.room)
        self.fields['seat'].queryset = seats

    def clean_seat(self):
        seats = self.cleaned_data.get('seat')
        for seat in seats:
            if seat in self.booked_seats:
                raise forms.ValidationError

        return seats

    def clean(self):
        self.clean_seat()
        return self.cleaned_data

    def save(self, user):
        tickets = []
        for seat in self.cleaned_data.get('seat'):
            ticket = Ticket.objects.create(
                user=user,
                session=self.session,
                seat=seat,
            )
            ticket.set_qr()
            tickets.append(ticket)
        return tickets
