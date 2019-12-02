from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuarios.views import register,AccountView
from apps.Progplay.views import detallePost,Preguntas, Juegos, QuienesSomos,tutoriales,generales,noticias,programacion,Blog



urlpatterns = [
    path('PreguntasFrecuentes/',Preguntas,name='Preguntas'),
    path('Juegos/',Juegos,name='Juegos'),
    path('Contactos/',register,name='Contactos'),
    path('QuienesSomos/',QuienesSomos,name='QuienesSomos'),
    path('perfil/',login_required(AccountView.as_view()),name='Perfil'),
    path('generales/',login_required(generales), name='generales'),
    path('tutoriales/',login_required(tutoriales), name='tutoriales'),
    path('noticias/',login_required(noticias), name='noticias'),
    path('programacion/',login_required(programacion),name='programacion'),
    path('Blog/',login_required(Blog),name='Blog'),
    path('<slug:slug>',login_required(detallePost),name='detallePost'),
    
]