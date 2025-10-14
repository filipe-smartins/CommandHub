from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from .models import Categoria, Comando, Secao

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome da categoria'})
        }

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['secao']
        widgets = {
            'secao': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome da seção'})
        }

class ComandoForm(forms.ModelForm):
    class Meta:
        model = Comando
        fields = ['comando', 'comentario', 'imagem']
        widgets = {
            'comando': forms.Textarea(attrs={'class': 'input', 'rows': 3, 'placeholder': 'Cole o comando aqui...'}),
            'comentario': forms.Textarea(attrs={'class': 'input', 'rows': 2, 'placeholder': 'Comentário opcional'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'input'})
        }


from .models import Artigo


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'arquivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Título do artigo'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'input'})
        }

    def clean_arquivo(self):
        f = self.cleaned_data.get('arquivo')
        if not f:
            return f
        allowed = ['pdf', 'docx', 'doc', 'txt', 'md']
        name = f.name.lower()
        if not any(name.endswith('.' + ext) for ext in allowed):
            raise ValidationError('Tipo de arquivo não permitido. Use: %s' % ', '.join(allowed))
        limit = 10 * 1024 * 1024  # 10 MB
        if f.size > limit:
            raise ValidationError('Arquivo muito grande (máx %s).' % filesizeformat(limit))
        return f