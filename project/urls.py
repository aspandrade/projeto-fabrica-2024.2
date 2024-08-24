from django.contrib import admin
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('usuarios/create/', views.create_usuario, name='create_usuario'),
    path('usuarios/<int:pk>/update/', views.update_usuario, name='update_usuario'),
    path('usuarios/<int:pk>/delete/', views.delete_usuario, name='delete_usuario'),
]
