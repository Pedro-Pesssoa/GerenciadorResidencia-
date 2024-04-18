from django.contrib import admin

from .models.taxa import Taxa
from .models.acompanhamento_taxa import AcompanhamentoTaxa

@admin.register(Taxa)
class TaxaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'valor',
        'data',
    ]

    search_fields = [
        'id',
        'valor',
        'data',
    ]

@admin.register(AcompanhamentoTaxa)
class AcompanhamentoTaxaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'taxa',
        'usuario',
        'comprovante',
        'comentario',
    ]

    search_fields = [
        'id',
        'taxa',
        'usuario',
        'comprovante',
        'comentario',
    ]

    list_filter = [
        'taxa',
        'usuario',
    ]

    autocomplete_fields = [
        'taxa',
        'usuario',
    ]

