from django.db import models


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)

class Foro(models.Model):
    id_creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Creador_Foro', default='')
    titulo = models.CharField(max_length=50, blank=True, default='')
    contenido = models.TextField(blank=True, default='')
    categoria = models.CharField(blank=True, max_length=10, default='')
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    imagen = models.TextField(blank=True, null=True, default='')
    class Meta:
        ordering=('fecha_creacion', 'titulo')

class Comentario(models.Model):
    id_participante = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name='Participante_Foro')
    id_foro = models.ForeignKey(Foro, on_delete = models.CASCADE, related_name='Foro_comentado')
    comentario = models.TextField(blank=True, null=True, default='')
    fecha_creacion =  models.DateField(auto_now=False, auto_now_add=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50, unique=True)
    class Meta:
        ordering=('nombre',)

class ClasificacionForo(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, related_name = 'Categoria_Foro')
    id_foro = models.ForeignKey(Foro, on_delete = models.CASCADE, related_name = 'Foro_a_clasificar')

