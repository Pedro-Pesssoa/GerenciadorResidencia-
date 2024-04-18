from django.db import models


class Taxa(models.Model):
    valor = models.FloatField(
        verbose_name="Valor"
    )

    data = models.DateField()

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f'Taxa {self.data}'

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'TaxaApp'
        verbose_name = 'Taxa'
        verbose_name_plural = 'Taxas'
