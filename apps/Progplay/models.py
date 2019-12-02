from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Pais(models.Model):
    idPais = models.AutoField(primary_key=True)
    NombrePais = models.CharField('Nombre del Pais', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name= 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['NombrePais']

    def __str__(self):
        return self.NombrePais

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    Nickname = models.CharField('Nickname', max_length=20, blank=False, null=False)
    NombreUsuario = models.CharField('Nombre del Usuario', max_length=50, blank=False, null=False)
    ClaveUsuario = models.CharField('Contraseña del Usuario', max_length=16, blank=False, null=False)
    Correo = models.EmailField('Correo del Usuario', max_length=80)
    ImagenPerfil = models.ImageField('Imagen de perfil', default=True, null=False)
    idPais = models.ForeignKey(Pais, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.NombreUsuario

class TipoUsuario(models.Model):
    idTipo = models.AutoField(primary_key=True)
    NombreTipoUsuario = models.CharField('Tipo de Usuario', max_length=20, null=False, blank=False) 
    idUsuario = models.OneToOneField(Usuarios, null=True, blank=True, on_delete=models.DO_NOTHING)

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField('Nombre de la Categoria', max_length=20, null=False, blank=False)
    Estado = models.BooleanField('Categoria activada / Categoria no activada', default=True)
    Fecha_Creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.NombreCategoria

class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    Pregunta = models.CharField('Pregunta', max_length=500, null=False, blank=False)
    Respuesta1 = models.CharField('Respuesta 1', max_length=100, null=False, blank=False)
    Respuesta2 = models.CharField('Respuesta 2', max_length=100, null=False, blank=False)
    Respuesta3 = models.CharField('Respuesta 3', max_length=100, null=False, blank=False)
    idCategoria = models.ForeignKey(Categoria, null=False, blank=False, on_delete=models.DO_NOTHING)

class Puntos_Categoria(models.Model):
    idPuntaje = models.AutoField(primary_key=True)
    Puntos = models.IntegerField('Puntaje', null=False, blank=False)
    idCategoria = models.OneToOneField(Categoria, null=True, blank=True, on_delete=models.DO_NOTHING)

class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado / No Publicado', default=True)
    fecha_creacion_post = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Logro(models.Model):
    idLogro = models.AutoField(primary_key=True)
    NombreLogro = models.CharField('Nombre del Logro', max_length=30, null=False, blank=False)
    ImagenLogro = models.ImageField('Imagen del Logro')
    Puntaje_Minimo = models.IntegerField('Puntaje Minimo Requerido', null=False, blank=False)
    Fecha_Logro = models.DateField('Fecha de logro adquirido', null=True, blank=True, auto_now=False, auto_now_add=True)
    idPuntaje = models.OneToOneField(Puntos_Categoria, null=True, blank=True, on_delete=models.DO_NOTHING)

class PuntajeUsuario(models.Model):
    idPuntajeUsuario = models.AutoField(primary_key=True)
    Puntaje_Acumulado = models.IntegerField('Puntaje Total', null=False, blank=False)
    idLogro = models.ForeignKey(Logro, null=True, blank=True, on_delete=models.DO_NOTHING)
    idUsuario = models.ForeignKey(Usuarios, null=True, blank=True, on_delete=models.DO_NOTHING)
    IdPuntaje = models.ForeignKey(Puntos_Categoria, null=True, blank=True, on_delete=models.DO_NOTHING)