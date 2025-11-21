from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    endereco = models.CharField("Endereço", max_length=255, blank=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    foto = models.ImageField("Foto de Perfil", upload_to="usuarios/fotos/", blank=True, null=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.username
