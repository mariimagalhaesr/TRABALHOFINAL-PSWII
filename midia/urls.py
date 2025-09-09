# midia/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_midias, name='listar_midias'),
    path('excluir/<int:midia_id>/', views.deletar_midia, name='deletar_midia'),
]