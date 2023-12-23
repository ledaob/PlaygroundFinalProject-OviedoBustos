from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'titulo', 'subtitulo', 'cuerpo', 'imagen', 'fecha', 'lugar']
    list_filter = ['nombre', 'titulo', 'fecha']
    search_fields = ['nombre', 'titulo']


