from django.urls import path, include

from .views import list_session

urlpatterns = [
    path('list/', list_session, name='list_session')
]
