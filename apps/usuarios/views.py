from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin
from django.contrib.auth.models import User
from apps.Progplay.models import Usuarios,Pais



class Login(FormView):
    template_name = 'Progplay/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Blog:Perfil')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)


    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def register(request):
    if request.POST:
        Nickname = request.POST.get('Nickname', False)
        NombreUsuario = request.POST.get('NombreUsuario', False)
        ClaveUsuario = request.POST.get('ClaveUsuario', False)
        ClaveUsuario2 = request.POST.get('ClaveUsuario' , False)
        Correo = request.POST.get('Correo', False)
        ImagenPerfil = ('apps/Progplay/static/Progplay/img/perfil.jpg')
        idPais = request.POST.get('idPais')
        p = Pais.objects.get(idPais=idPais)

        v = Usuarios( Nickname=Nickname, NombreUsuario=NombreUsuario,ClaveUsuario=ClaveUsuario,Correo=Correo,idPais = p,ImagenPerfil=ImagenPerfil)
        if(ClaveUsuario == ClaveUsuario2):
            u = User.objects.create_user(
            username=Nickname, first_name=NombreUsuario,password=ClaveUsuario,email=Correo
            )
            v.save()
            u.save()
            return render(request,'Progplay/completado.html')

            
    context = {'Pais':Pais.objects.all()}
    return render(request,'Progplay/Contactos.html', context)




class AccountView(ListView):
    model = Usuarios
    template_name = 'Progplay/perfil.html'

def get_queryset(self):

        datos = Usuarios.objects.get(Nickname=self.request.user.username)
    
        return render(self.request,'Progplay/perfil.html',{'datos':datos})


def listarAutor(request):
    usuarios = Usuarios.objects.get(
       Nickname=request.user.username
    )
    return render(request,'Progplay/perfil.html',{'usuarios':usuarios})



def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')



        
         






