# categoria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_categorias'),
    path('criar/', views.criar, name='criar_categoria'),
    path('editar/<int:categoria_id>/', views.editar, name='editar_categoria'),
    path('deletar/<int:categoria_id>/', views.deletar, name='deletar_categoria'),
]