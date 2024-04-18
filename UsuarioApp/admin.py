from django.contrib import admin

from .usuario import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'ala',
        'quarto',
        'lider',
        'em_dia_limpeza',
        'em_dia_taxa',
    ]

    search_fields = [
        'user',
        'ala',
        'quarto',
        'lider',
        'em_dia_limpeza',
        'em_dia_taxa',
    ]

    list_filter = [
        'user',
        'lider',
        'em_dia_limpeza',
        'em_dia_taxa',
    ]

    autocomplete_fields = [
        'user',
    ]
