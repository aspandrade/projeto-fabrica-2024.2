from django.contrib import admin
from django.urls import path, include
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('app_cad_usuarios.urls')),  
]
