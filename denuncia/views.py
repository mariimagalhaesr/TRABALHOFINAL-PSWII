from django.shortcuts import render, redirect
from .forms import DenunciaForm

def enviar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('denuncia_sucesso')  # Redireciona para uma página de sucesso
    else:
        form = DenunciaForm()
    
    # Corrigido o caminho do template
    return render(request, 'denuncia/denuncia_form.html', {'form': form})

def denuncia_sucesso(request):
    return render(request, 'denuncia/denuncia_sucesso.html')
