from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_usuario'),
    path('cadastrar/', views.cadastrar, name='cadastrar_usuario'),
    path('editar/<int:usuario_id>/', views.editar, name='editar_usuario'),
    path('detalhar/<int:usuario_id>/', views.detalhar, name='detalhar_usuario'),
    path('deletar/<int:usuario_id>/', views.deletar, name='deletar_usuario'),
    path('painel/', views.painel_denuncias, name='painel_denuncias'),
]