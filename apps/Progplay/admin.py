from django.contrib import admin
from .models import Pais, Usuarios, TipoUsuario, Categoria, Puntos_Categoria, Logro, PuntajeUsuario, Pregunta, Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NombreCategoria']
    list_display = ('NombreCategoria','Estado',)
    resource_class = CategoriaResource

class PaisResource(resources.ModelResource):
    class Meta:
        model = Pais

class PaisAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NombrePais']
    list_display = ('NombrePais',)
    resource_class = PaisResource

class UsuariosResource(resources.ModelResource):
    class Meta:
        model = Usuarios

class UsuariosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Nickname', 'NombreUsuario']
    list_display = ('Nickname', 'NombreUsuario', 'Correo',)
    resource_class = UsuariosResource

class TipoUsuarioResource(resources.ModelResource):
    class Meta:
        model = TipoUsuario

class TipoUsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NombreUsuario']
    list_display = ('idTipo', 'NombreTipoUsuario',)
    resource_class = TipoUsuarioResource

class Puntos_CategoriaResource(resources.ModelResource):
    class Meta:
        model = Puntos_Categoria

class Puntos_CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Puntos']
    list_display = ('Puntos',)
    resource_class = Puntos_CategoriaResource

class LogroResource(resources.ModelResource):
    class Meta:
        model = Logro

class LogroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['NombreLogro']
    resource_class = LogroResource

class PuntajeUsuarioResource(resources.ModelResource):
    class Meta:
        model = PuntajeUsuario

class PuntajeUsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Puntaje_Acumulado']
    resource_class = PuntajeUsuarioResource

class PreguntaResource(resources.ModelResource):
    class Meta:
        model = Pregunta

class PreguntaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['idPregunta']
    list_display = ('Pregunta',)
    resource_class = PreguntaResource

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['Titulo']
    list_display = ('idPost', 'titulo', 'fecha_creacion_post',)
    resource_class = PostResource



# Register your models here.

admin.site.register(Pais, PaisAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Puntos_Categoria, Puntos_CategoriaAdmin)
admin.site.register(Logro, LogroAdmin)
admin.site.register(PuntajeUsuario, PuntajeUsuarioAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Post, PostAdmin)