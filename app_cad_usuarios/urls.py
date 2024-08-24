from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('usuarios/criar/', views.create_usuario, name='criar_usuario'),
    path('usuarios/editar/<int:id>/', views.update_usuario, name='editar_usuario'),
    path('usuarios/deletar/<int:id>/', views.delete_usuario, name='deletar_usuario'),
]
