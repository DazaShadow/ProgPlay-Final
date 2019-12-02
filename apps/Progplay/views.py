from django.shortcuts import render,redirect
from apps.usuarios.forms import FormularioLogin
from .models import Usuarios,Post,Categoria
from django.views.generic import TemplateView,UpdateView
from django.db.models import Q
from django.urls import reverse_lazy

class Inicio(TemplateView):
  def get(self,request,*args,**kwargs):
      return render(request,'Progplay/index.html')


#def crearUsuario(request):
    #if request.method == 'POST':
        #usuario_form = UsuarioForm(request.POST)
        #if usuario_form.is_valid():
           # usuario_form.save()
           # return redirect('Inicio')
   # else:
      #  usuario_form = UsuarioForm()
       # return render(request,'ProgPlay/Contactos.html',{'usuario_form':usuario_form})


#class ActualizarUsuario(UpdateView):
    #model = Usuarios
    #template_name = 'ProgPlay/Contactos.html'
    #form_class = UsuarioForm
    #success_url = reverse_lazy('Blog:Blog')


def Preguntas(request):
    return render(request,'Progplay/PreguntasFrecuentes.html')

def Juegos(request):
    return render(request,'Progplay/Juegos.html')


def QuienesSomos(request):
    return render(request,'Progplay/QuienesSomos.html')



def Blog(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    posts = Post.objects.filter(estado=True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    return render(request, 'Progplay/Blog.html', {'posts':posts})


def login(request):
    return render(request,'Progplay/login.html')  


def generales(request):
    queryset = request.GET.get("buscar")
    print(queryset)

    posts = Post.objects.filter(
        estado = True,
        idCategoria = Categoria.objects.get(NombreCategoria__iexact = 'Generales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            idCategoria = Categoria.objects.get(NombreCategoria__iexact = 'Generales'),
        ).distinct()
    return render(request,'Progplay/generales.html',{'posts':posts})  


def tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        idCategoria = Categoria.objects.get(NombreCategoria = 'Tutoriales')
    )
    return render(request,'Progplay/tutoriales.html',{'posts':posts})  


def noticias(request):
    posts = Post.objects.filter(
        estado = True,
        idCategoria = Categoria.objects.get(NombreCategoria = 'Noticias')
    )
    return render(request,'Progplay/noticias.html',{'posts':posts})  


def programacion(request):
    posts = Post.objects.filter(
        estado = True,
        idCategoria = Categoria.objects.get(NombreCategoria = 'Programacion')
    )
    return render(request,'Progplay/programacion.html',{'posts':posts})  


def detallePost(request,slug):
    posts = Post.objects.get(
        
        slug = slug
    )
    print(posts)
    return render(request,'Progplay/post.html',{'detallePost':posts})




def password_reset(request):
    return render(request,'Recuperacion/password_reset_form.html')

def password_reset_complete(request):
    return render(request,'Recuperacion/password_reset_complete.html')

def password_reset_confirm(request):
    return render(request,'Recuperacion/password_reset_confirm.html')

def password_reset_email(request):
    return render(request,'Recuperacion/password_reset_email.html')

def password_reset_done(request):
    return render(request,'Recuperacion/password_reset_done.html')








  