from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'user_user'

    class Role(models.TextChoices):
        ADMIN = 'admin'
        USER = 'user'

    first_name = None
    last_name = None
    email = None
    role = models.CharField(max_length=255, choices=Role.choices, default=Role.USER)
