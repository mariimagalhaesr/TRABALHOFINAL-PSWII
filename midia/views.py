# midia/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Midia
from .forms import MidiaForm

@login_required
@permission_required('midia.view_midia', raise_exception=True)
def listar_midias(request):
    midias = Midia.objects.all().order_by('-id')
    return render(request, 'midia/listar.html', {'midias': midias})

@login_required
@permission_required('midia.add_midia', raise_exception=True)
def cadastrar_midia(request):
    if request.method == 'POST':
        form = MidiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_midias')
    else:
        form = MidiaForm()
    return render(request, 'midia/cadastrar.html', {'form': form})

@login_required
@permission_required('midia.delete_midia', raise_exception=True)
def deletar_midia(request, midia_id):
    midia = get_object_or_404(Midia, pk=midia_id)
    if request.method == 'POST':
        midia.arquivo.delete() # Deleta o arquivo físico
        midia.delete() # Deleta o registro do banco
        return redirect('listar_midias')
    return render(request, 'midia/confirm_delete.html', {'midia': midia})