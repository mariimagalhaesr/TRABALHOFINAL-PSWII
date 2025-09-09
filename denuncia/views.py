from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DenunciaAnonimaForm, DenunciaStatusForm, ConsultaStatusForm
from .models import Denuncia
from midia.models import Midia
from midia_denuncia.models import MidiaDenuncia

def enviar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaAnonimaForm(request.POST, request.FILES)
        if form.is_valid():
            denuncia = form.save()
            files = request.FILES.getlist('arquivos_prova')

            for f in files:
                # --- LÓGICA DE DETECÇÃO DO TIPO DE MÍDIA ---
                content_type = f.content_type
                if content_type.startswith('image'):
                    tipo_midia = 'imagem'
                elif content_type.startswith('audio'):
                    tipo_midia = 'audio'
                elif content_type.startswith('video'):
                    tipo_midia = 'video'
                else:
                    tipo_midia = 'outro'

                nova_midia = Midia.objects.create(
                    nome=f.name,
                    tipo=tipo_midia, # Usando a variável com o tipo correto
                    arquivo=f
                )

                MidiaDenuncia.objects.create(
                    denuncia=denuncia,
                    midia=nova_midia,
                    # O campo 'conteudo' é redundante, veja a otimização abaixo
                    conteudo=f
                )

            return redirect('sucesso_denuncia', codigo_rastreamento=denuncia.codigo_rastreamento)
    else:
        form = DenunciaAnonimaForm()

    return render(request, 'denuncia/denuncia_form.html', {'form': form})

def sucesso_denuncia(request, codigo_rastreamento):
    return render(request, 'denuncia/sucesso.html', {'codigo': codigo_rastreamento})


@login_required
def listar_denuncia(request):

    denuncias = Denuncia.objects.all().order_by('-dt_envio')
    return render(request, 'denuncia/listar.html', {'denuncias': denuncias})

@login_required
def detalhar_denuncia(request, denuncia_id):

    denuncia = get_object_or_404(Denuncia, pk=denuncia_id)
    
    if request.method == 'POST':

        form = DenunciaStatusForm(request.POST, instance=denuncia)
        if form.is_valid():
            form.save()

            return redirect('listar_denuncia') 
    else:

        form = DenunciaStatusForm(instance=denuncia)

    provas = MidiaDenuncia.objects.filter(denuncia=denuncia)

    context = {
        'denuncia': denuncia,
        'form': form,
        'provas': provas
    }
    return render(request, 'denuncia/detalhar.html', context)

def consultar_denuncia(request):
    denuncia = None
    if request.method == 'POST':
        form = ConsultaStatusForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            try:

                denuncia = Denuncia.objects.get(codigo_rastreamento=codigo)
            except Denuncia.DoesNotExist:

                form.add_error('codigo', 'Código de rastreamento inválido ou não encontrado.')
    else:
        form = ConsultaStatusForm()

    return render(request, 'denuncia/consultar_status.html', {'form': form, 'denuncia': denuncia})