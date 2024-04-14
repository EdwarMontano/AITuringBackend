from django.contrib.auth.models import AbstractUser
from django.db import models


# Own Libraries
from user_managment.models.usuarios import BaseAbstractModel


class User(AbstractUser, BaseAbstractModel):
    email = models.EmailField("email address", unique=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        db_table = "auth_user"
