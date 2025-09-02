# midia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_midias, name='listar_midias'),
    path('cadastrar/', views.cadastrar_midia, name='cadastrar_midia'),
    path('deletar/<int:midia_id>/', views.deletar_midia, name='deletar_midia'),
]