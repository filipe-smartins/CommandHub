from django import forms
from .models import Categoria, Comando, Secao

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['secao']

class ComandoForm(forms.ModelForm):
    class Meta:
        model = Comando
        fields = ['comando', 'comentario', 'imagem']