from django.urls import path, include

from . import views

urlpatterns = [
    path('pay/<int:session_id>', views.get_purchase_ticket_form, name='pay_tickets'),
    path('', views.tickets, name='tickets'),
    path('check_ticket/<int:ticket_id>', views.check_ticket, name='check_ticket'),

]
