from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    ALA_CHOICES = (
        ("Ala 1", "Ala 1"),
        ("Ala 2", "Ala 2"),
        ("Ala 3", "Ala 3"),
        ("Ala 4", "Ala 4"),
    )

    ala = models.CharField(
        verbose_name="Ala",
        max_length=10,
        choices=ALA_CHOICES,
    )

    quarto = models.IntegerField(
        verbose_name="Quarto",
        max_length=1,
    )
    
    lider = models.BooleanField(
        verbose_name="Lider de ala",
        default=False,
    )

    em_dia_limpeza = models.BooleanField(
        verbose_name="Em dia com a Limpeza",
        default=False,
    )

    em_dia_taxa = models.BooleanField(
        verbose_name="Em dia com a Taxa",
        default=False,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f'{self.user}'

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'LimpezaApp'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
