from django.db import models
from .limpeza import Limpeza
from django.contrib.auth.models import User

class AcompanhamentoLimpeza(models.Model):

    limpeza = models.ForeignKey(
        Limpeza,
        verbose_name='Limpeza',
        on_delete=models.CASCADE,
    )

    usuario = models.ForeignKey(
        User, 
        verbose_name='Usuario',
        on_delete=models.CASCADE
    )

    comentario = models.TextField(
        verbose_name='comentario',
        max_length=1000,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f'{self.usuario} - {self.limpeza}'

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'LimpezaApp'
        verbose_name = 'Gerenciador de Limpeza'
        verbose_name_plural = 'Gerenciador de Limpezas'
