from django import forms
from .models.acompanhamento_limpeza import AcompanhamentoLimpeza

class AcompanhamentoLimpezaForm(forms.ModelForm):
    class Meta:
        model = AcompanhamentoLimpeza
        fields = ['limpeza', 'comodo', 'usuario', 'comentario']