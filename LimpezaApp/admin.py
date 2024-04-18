from django.contrib import admin

from .models.limpeza import Limpeza
from .models.acompanhamento_limpeza import AcompanhamentoLimpeza

@admin.register(Limpeza)
class LimpezaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ala',
        'data',
    ]

    search_fields = [
        'id',
        'ala',
        'data',
    ]

    # def has_change_permission(self, request, obj=None):
    #     # Permitir apenas superusuários
    #     return request.user.is_superuser

@admin.register(AcompanhamentoLimpeza)
class AcompanhamentoLimpezaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'limpeza',
        'usuario',
        'comentario',   
    ]

    search_fields = [
        'id',
        'limpeza',
        'usuario',
        'comentario',   
    ]

    list_filter = [
        'limpeza',
        'usuario',
    ]

    autocomplete_fields = [
        'limpeza',
        'usuario',
    ]
