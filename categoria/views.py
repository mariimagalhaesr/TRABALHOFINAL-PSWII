# categoria/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Categoria
from .forms import CategoriaForm

@login_required
@permission_required('categoria.view_categoria', raise_exception=True)
def listar(request):
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'categoria/listar.html', {'categorias': categorias})

@login_required
@permission_required('categoria.add_categoria', raise_exception=True)
def criar(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categoria/criar.html', {'form': form})

@login_required
@permission_required('categoria.change_categoria', raise_exception=True)
def editar(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/editar.html', {'form': form, 'categoria': categoria})

@login_required
@permission_required('categoria.delete_categoria', raise_exception=True)
def deletar(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'categoria/confirmar_delete.html', {'categoria': categoria})