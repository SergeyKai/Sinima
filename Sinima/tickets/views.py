from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PurchaseTicketForm

from cinemas.models import Session
from .models import Ticket


@login_required
def get_purchase_ticket_form(request, session_id):
    session = Session.objects.get(pk=session_id)

    if request.method == 'POST':
        form = PurchaseTicketForm(data=request.POST, session=session)
        if form.is_valid():
            form.save(request.user)
            return redirect(reverse('tickets'))

    else:
        form = PurchaseTicketForm(session)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'session': session})


@login_required
def tickets(request):
    u_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets/tickets.html', {'tickets': u_tickets})


@login_required
def check_ticket(request, ticket_id):
    return render(request, 'tickets/check_success.html')
