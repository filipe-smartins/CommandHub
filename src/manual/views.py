# View para editar Categoria
def categoria_edit(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'manual/categoria_edit.html', {'form': form, 'categoria': categoria})

# View para deletar Categoria
def categoria_delete(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('home')
    return render(request, 'manual/categoria_delete.html', {'categoria': categoria})

# View para editar Seção
def secao_edit(request, secao_id):
    secao = get_object_or_404(Secao, id=secao_id)
    if request.method == 'POST':
        form = SecaoForm(request.POST, instance=secao)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SecaoForm(instance=secao)
    return render(request, 'manual/secao_edit.html', {'form': form, 'secao': secao})

# View para deletar Seção
def secao_delete(request, secao_id):
    secao = get_object_or_404(Secao, id=secao_id)
    if request.method == 'POST':
        secao.delete()
        return redirect('home')
    return render(request, 'manual/secao_delete.html', {'secao': secao})
# View para adicionar Seção a uma Categoria
def secao_add(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = SecaoForm(request.POST)
        if form.is_valid():
            secao = form.save(commit=False)
            secao.categoria = categoria
            secao.save()
            return redirect('home')
    else:
        form = SecaoForm()
    return render(request, 'manual/secao_add.html', {'form': form, 'categoria': categoria})
# View para deletar Tipo
from django.urls import reverse
from django.http import HttpResponseRedirect
def tipo_delete(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('home')
    return render(request, 'manual/tipo_delete.html', {'tipo': tipo})
# View para editar Tipo
def tipo_edit(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TipoForm(instance=tipo)
    return render(request, 'manual/tipo_edit.html', {'form': form, 'tipo': tipo})
# View para adicionar Categoria a um Tipo
def categoria_add(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.tipo = tipo
            categoria.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'manual/categoria_add.html', {'form': form, 'tipo': tipo})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tipo, Categoria, Secao, Comando
from .forms import CategoriaForm, ComandoForm, SecaoForm
from django import forms

# Formulário para adicionar Tipo
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['tipo']

# View para adicionar Tipo
def tipo_add(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TipoForm()
    return render(request, 'manual/tipo_add.html', {'form': form})

def home(request):
    tipos = Tipo.objects.prefetch_related('categorias__secoes').all()
    return render(request, "manual/home.html", {"tipos": tipos})

def tipo_detail(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    categorias = tipo.categorias.all().order_by('nome')
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.tipo = tipo
            categoria.save()
            return redirect("tipo_detail", tipo_id=tipo.id)
    else:
        form = CategoriaForm()
    return render(request, "manual/tipo_detail.html", {"tipo": tipo, "categorias": categorias, "form": form})

def categoria_detail(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    secoes = categoria.secoes.all().order_by('secao')
    if request.method == "POST":
        form = SecaoForm(request.POST)
        if form.is_valid():
            secao = form.save(commit=False)
            secao.categoria = categoria
            secao.save()
            return redirect("categoria_detail", categoria_id=categoria.id)
    else:
        form = SecaoForm()
    return render(request, "manual/categoria_detail.html", {"categoria": categoria, "secoes": secoes, "form": form})

def secao_detail(request, secao_id):
    secao = get_object_or_404(Secao, id=secao_id)
    comandos = secao.comandos.all().order_by("-criado_em")
    if request.method == "POST":
        form = ComandoForm(request.POST, request.FILES)
        if form.is_valid():
            comando = form.save(commit=False)
            comando.secao = secao
            comando.save()
            return redirect("secao_detail", secao_id=secao.id)
    else:
        form = ComandoForm(initial={"secao": secao})
    return render(request, "manual/secao_detail.html", {"secao": secao, "comandos": comandos, "form": form})
