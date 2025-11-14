from django.contrib import admin

from .models import Categoria, Despesa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ("nome",)


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "valor", "data")
    list_filter = ("categoria", "data")
    search_fields = ("titulo", "observacoes")
    autocomplete_fields = ("categoria",)
