from django.urls import path, include

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    path('change_password/', PasswordChangeView.as_view(template_name='users/user_change_data.html'), name='change_password'),
    path('change_password_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('user_change_data/', views.user_change_data, name='user_change_data'),
]
