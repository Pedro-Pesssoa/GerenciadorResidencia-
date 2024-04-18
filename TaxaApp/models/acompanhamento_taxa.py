from django.db import models
from .taxa import Taxa
from django.contrib.auth.models import User

class AcompanhamentoTaxa(models.Model):
    taxa = models.ForeignKey(
        Taxa,
        verbose_name='Taxa',
        on_delete=models.CASCADE,
    )

    usuario = models.ForeignKey(
        User, 
        verbose_name='Usuario',
        on_delete=models.CASCADE
    )

    comprovante = models.FileField(
        verbose_name='Comprovante', 
        upload_to="",
    )

    comentario = models.TextField(
        verbose_name='comentario',
        max_length=1000,
    )

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'TaxaApp'
        verbose_name = 'Acompanhamento da taxa'
        verbose_name_plural = 'Acompanhamento das taxas'
