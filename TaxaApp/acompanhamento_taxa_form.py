from django import forms
from .models.acompanhamento_taxa import AcompanhamentoTaxa

class AcompanhamentoTaxaForm(forms.ModelForm):
    class Meta:
        model = AcompanhamentoTaxa
        fields = ['taxa', 'usuario', 'comprovante', 'comentario']