from django import forms
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label='Пароль',
        help_text="""
        Для смены пароля перейдите по этой ссылке
        <a href="/users/change_password/">Изменить пароль</a>
        """,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'email')
