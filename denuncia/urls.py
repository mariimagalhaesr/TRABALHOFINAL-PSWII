from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_denuncia, name='enviar_denuncia'),
    path('sucesso/<str:codigo_rastreamento>/', views.sucesso_denuncia, name='sucesso_denuncia'),
    path('consultar/', views.consultar_denuncia, name='consultar_denuncia'),
    path('', views.listar_denuncia, name='listar_denuncia'),
    path('<int:denuncia_id>/', views.detalhar_denuncia, name='detalhar_denuncia'),
]
