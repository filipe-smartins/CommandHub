from django.contrib import admin
from .models import Tipo, Categoria, Secao, Comando

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo")
    search_fields = ("tipo",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "tipo")
    list_filter = ("tipo",)
    search_fields = ("nome",)

@admin.register(Secao)
class SecaoAdmin(admin.ModelAdmin):
    list_display = ("id", "secao", "categoria")
    list_filter = ("categoria",)
    search_fields = ("secao",)

@admin.register(Comando)
class ComandoAdmin(admin.ModelAdmin):
    list_display = ("id", "secao", "comando", "criado_em")
    list_filter = ("secao",)
    search_fields = ("comando", "comentario")
