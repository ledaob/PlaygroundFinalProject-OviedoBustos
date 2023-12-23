from django.contrib import admin
from django.urls import path
from Proyecto import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Proyecto'

urlpatterns = [
    path('inicio/', views.inicio, name= "inicio"),
    path('acercademi/', views.acercaDeMi, name="acercaDeMi"),
    path('verPost/<int:pk>/', views.PostDetailView.as_view(), name='ver_posts'),
    path('pages/', views.lista_blogs, name='lista_blogs'),



    

    


] + static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)