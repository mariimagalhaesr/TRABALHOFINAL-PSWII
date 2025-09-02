from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Usuario 
from .forms import UsuarioForm, UsuarioEditForm
from denuncia.models import Denuncia
from categoria.models import Categoria 

@login_required
@permission_required('auth.view_user', raise_exception=True) 
def index(request):

    usuarios = Usuario.objects.all().order_by('first_name') 
    return render(request, 'usuario/index.html', {'usuarios': usuarios})

@login_required
@permission_required('auth.add_user', raise_exception=True)
def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/cadastrar.html', {'form': form})

@login_required
@permission_required('auth.view_user', raise_exception=True) 

def detalhar(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    return render(request, 'usuario/detalhar.html', {'usuario': usuario})

@login_required
@permission_required('auth.change_user', raise_exception=True)

def editar(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()

            return redirect('index_usuario')
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'usuario/editar.html', {'form': form, 'usuario': usuario})

@login_required
@permission_required('auth.delete_user', raise_exception=True)

def deletar(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('index_usuario')

    return render(request, 'usuario/confirm_delete.html', {'usuario': usuario})

@login_required
def painel_denuncias(request):
    todas_denuncias = Denuncia.objects.all()
    todas_categorias = Categoria.objects.all()
    total_denuncias = todas_denuncias.count()
    denuncias_em_andamento = todas_denuncias.filter(status='em_andamento').count()
    denuncias_finalizadas = todas_denuncias.filter(status='finalizada').count()

    context = {

        'denuncias': todas_denuncias.order_by('-dt_envio'),
        'categorias': todas_categorias, 
        'total_denuncias': total_denuncias,
        'denuncias_em_andamento': denuncias_em_andamento,
        'denuncias_finalizadas': denuncias_finalizadas,
    }
    return render(request, 'usuario/painel.html', context)