from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django import forms
import json
from .models import Tipo, Categoria, Secao, Comando, Artigo
from .forms import CategoriaForm, ComandoForm, SecaoForm, ArtigoForm


# Formulário para adicionar Tipo
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['tipo']


# ========== VIEWS PÚBLICAS (não requerem login) ==========

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
    # support filtering view: commands | articles | all
    view_mode = request.GET.get('view', 'all')
    comandos = secao.comandos.all().order_by("ordem", "-criado_em")
    artigos = secao.artigos.all().order_by("-criado_em")

    # ensure forms exist
    cform = ComandoForm(initial={"secao": secao})
    aform = ArtigoForm()

    if request.method == "POST" and request.user.is_authenticated:
        if 'comando_submit' in request.POST:
            cform = ComandoForm(request.POST, request.FILES)
            if cform.is_valid():
                comando = cform.save(commit=False)
                comando.secao = secao
                comando.autor = request.user
                comando.save()
                return redirect("secao_detail", secao_id=secao.id)
        elif 'artigo_submit' in request.POST:
            aform = ArtigoForm(request.POST, request.FILES)
            if aform.is_valid():
                artigo = aform.save(commit=False)
                artigo.secao = secao
                artigo.autor = request.user
                artigo.save()
                return redirect("secao_detail", secao_id=secao.id)

    context = {
        "secao": secao,
        "comandos": comandos,
        "artigos": artigos,
        "cform": cform,
        "aform": aform,
        "view_mode": view_mode,
    }
    return render(request, "manual/secao_detail.html", context)


# ========== TIPO - CRUD (requer login) ==========

@login_required
def tipo_add(request):
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.autor = request.user
            tipo.save()
            return redirect('home')
    else:
        form = TipoForm()
    return render(request, 'manual/tipo_add.html', {'form': form})


@login_required
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


@login_required
def tipo_delete(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('home')
    return render(request, 'manual/tipo_delete.html', {'tipo': tipo})


# ========== CATEGORIA - CRUD (requer login) ==========

@login_required
def categoria_add(request, tipo_id):
    tipo = get_object_or_404(Tipo, id=tipo_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.tipo = tipo
            categoria.autor = request.user
            categoria.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'manual/categoria_add.html', {'form': form, 'tipo': tipo})


@login_required
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


@login_required
def categoria_delete(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('home')
    return render(request, 'manual/categoria_delete.html', {'categoria': categoria})


# ========== SECAO - CRUD (requer login) ==========

@login_required
def secao_add(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = SecaoForm(request.POST)
        if form.is_valid():
            secao = form.save(commit=False)
            secao.categoria = categoria
            secao.autor = request.user
            secao.save()
            return redirect('home')
    else:
        form = SecaoForm()
    return render(request, 'manual/secao_add.html', {'form': form, 'categoria': categoria})


@login_required
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


@login_required
def secao_delete(request, secao_id):
    secao = get_object_or_404(Secao, id=secao_id)
    if request.method == 'POST':
        secao.delete()
        return redirect('home')
    return render(request, 'manual/secao_delete.html', {'secao': secao})


# ========== COMANDO - CRUD (requer login) ==========

@login_required
def comando_edit(request, comando_id):
    comando = get_object_or_404(Comando, id=comando_id)
    if request.method == 'POST':
        form = ComandoForm(request.POST, request.FILES, instance=comando)
        if form.is_valid():
            form.save()
            return redirect('secao_detail', secao_id=comando.secao.id)
    else:
        form = ComandoForm(instance=comando)
    return render(request, 'manual/comando_edit.html', {'form': form, 'comando': comando})


@login_required
def comando_delete(request, comando_id):
    comando = get_object_or_404(Comando, id=comando_id)
    secao_id = comando.secao.id
    if request.method == 'POST':
        comando.delete()
        return redirect('secao_detail', secao_id=secao_id)
    return render(request, 'manual/comando_delete.html', {'comando': comando})


# ========== ARTIGO - CRUD (requer login) ==========

@login_required
def artigo_edit(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('secao_detail', secao_id=artigo.secao.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'manual/artigo_edit.html', {'form': form, 'artigo': artigo})


@login_required
def artigo_delete(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    secao_id = artigo.secao.id
    if request.method == 'POST':
        artigo.arquivo.delete(save=False)
        artigo.delete()
        return redirect('secao_detail', secao_id=secao_id)
    return render(request, 'manual/artigo_delete.html', {'artigo': artigo})


# ========== REORDENAÇÃO DE COMANDOS ==========

@login_required
@require_POST
@csrf_exempt
def comando_reorder(request):
    """View para atualizar a ordem dos comandos via AJAX"""
    try:
        print("=== COMANDO REORDER ===")
        print(f"Request body: {request.body}")
        
        data = json.loads(request.body)
        ordem_ids = data.get('ordem', [])
        
        print(f"Ordem recebida: {ordem_ids}")
        
        # Atualiza a ordem de cada comando
        for index, comando_id in enumerate(ordem_ids):
            updated = Comando.objects.filter(id=comando_id).update(ordem=index)
            print(f"Comando {comando_id} -> ordem {index} (updated: {updated})")
        
        print("=== SUCESSO ===")
        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(f"=== ERRO: {str(e)} ===")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
