from django.contrib import admin

from .models.limpeza import Limpeza
from .models.acompanhamento_limpeza import AcompanhamentoLimpeza
from .acompanhamento_limpeza_form import AcompanhamentoLimpezaForm

@admin.register(Limpeza)
class LimpezaAdmin(admin.ModelAdmin):
    list_display = [
        'ala',
        'data',
    ]

    search_fields = [
        'ala',
        'data',
    ]

@admin.register(AcompanhamentoLimpeza)
class AcompanhamentoLimpezaAdmin(admin.ModelAdmin):
    form = AcompanhamentoLimpezaForm
    list_display = [
        'limpeza',
        'comodo',
        'usuario',
        'comentario',   
    ]

    search_fields = [
        'limpeza',
        'comodo',
        'usuario',
        'comentario',   
    ]

    list_filter = [
        'limpeza',
        'usuario',
        'comodo',
    ]

    autocomplete_fields = [
        'limpeza',
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
