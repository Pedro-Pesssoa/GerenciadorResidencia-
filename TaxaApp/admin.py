from django.contrib import admin

from .models.taxa import Taxa
from .models.acompanhamento_taxa import AcompanhamentoTaxa
from .acompanhamento_taxa_form import AcompanhamentoTaxaForm

@admin.register(Taxa)
class TaxaAdmin(admin.ModelAdmin):
    list_display = [
        'valor',
        'data',
    ]

    search_fields = [
        'valor',
        'data',
    ]

@admin.register(AcompanhamentoTaxa)
class AcompanhamentoTaxaAdmin(admin.ModelAdmin):
    form = AcompanhamentoTaxaForm
    list_display = [
        'taxa',
        'usuario',
        'comprovante',
        'comentario',
    ]

    search_fields = [
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

    def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            if not obj: 
                form.base_fields.pop('usuario', None) 
            return form

    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.usuario = request.user 
        super().save_model(request, obj, form, change)