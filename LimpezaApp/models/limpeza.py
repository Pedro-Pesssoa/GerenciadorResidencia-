from django.db import models


class Limpeza(models.Model):

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

    data = models.DateField()

    def __str__(self):
        '''Método que retorna a representação do objeto como string.'''
        return f"Limpeza dia {self.data}"

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'LimpezaApp'
        verbose_name = 'Limpeza'
        verbose_name_plural = 'Limpezas'
