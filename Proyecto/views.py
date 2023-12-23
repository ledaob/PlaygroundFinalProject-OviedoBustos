from django.shortcuts import  render, redirect
from Proyecto.models import *
from django.views.generic.detail import DetailView
from Proyecto.forms import *



def inicio (request):
    return render (request, 'Proyecto/index.html')


def acercaDeMi(request):
    return render(request, 'Proyecto/acercaDeMi.html')


class PostDetailView(DetailView):
    model= Post
    context_object_name= "posts"
    template_name = 'Proyecto/post_detail.html'

def lista_blogs(request):
    posts = Post.objects.all()
    return render (request, 'Proyecto/lista_blogs.html', {"posts": posts})