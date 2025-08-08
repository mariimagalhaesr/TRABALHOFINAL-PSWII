from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_denuncia, name='enviar_denuncia'),
    path('sucesso/', views.denuncia_sucesso, name='denuncia_sucesso'),
]
