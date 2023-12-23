from django.contrib import admin
from django.urls import path
from django import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views





app_name = 'accounts'

urlpatterns = [        
    path('login/', views.user_login, name= "login"),
    path('registro/', views.registro, name= "registro"),
    path('logout/', views.user_logout, name= "logout"),
    path('perfil/', views.perfil, name= "perfil"),
    path('perfil/editar/', views.editarPerfil, name="editarPerfil"),
    path('perfil/editar/', views.eliminar_perfil, name="borrarPerfil"),

    

    


] + static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)