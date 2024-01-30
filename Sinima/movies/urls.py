from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.movies_list, name='movies_list'),
    path('<slug:movie_slug>/', views.movie_detail, name='movie'),
    path('actor/<slug:actor_slug>/', views.actor_detail, name='actor'),
]
