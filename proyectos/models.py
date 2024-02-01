from django.db import models
from django.utils.translation import gettext_lazy
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Estado(models.Model):
    estado = models.CharField(max_length=50)
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='estado_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='estado_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))
    def __str__(self):
        return self.estado 

class Sprint(models.Model):
    sprint = models.CharField(max_length=50)
    fechaini = models.DateTimeField()
    fechafin = models.DateTimeField()
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='sprint_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='sprint_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.sprint 

class Proyecto(models.Model):
    proyecto = models.CharField(max_length=50)
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='proyecto_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='proyecto_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.proyecto 

class Empresa(models.Model):
    empresa = models.CharField(max_length=50)
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='empresa_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='empresa_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.empresa 

class Tipo_tarea(models.Model):
    tipo = models.CharField(max_length=50)
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tipo_tarea_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tipo_tarea_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))    
    def __str__(self):
        return self.tipo       

class Tarea(models.Model):
    titulo = models.CharField(max_length=500)
    #descripcion = RichTextField(verbose_name="Descripción")
    descripcion = models.TextField()
    fechaini = models.DateField()
    fechafin = models.DateField()
    tiempo_estimado = models.IntegerField()
    coste = models.DecimalField( decimal_places=2 , max_digits=16 )
    estado = models.ForeignKey(Estado, related_name='estado_tarea', on_delete=models.PROTECT)
    sprint = models.ForeignKey(Sprint, related_name='sprint_tarea', on_delete=models.PROTECT)
    proyecto = models.ForeignKey(Proyecto, related_name='proyecto_tarea', on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, related_name='empresa_tarea', on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo_tarea, related_name='tipo_tarea', on_delete=models.PROTECT)
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tarea_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tarea_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.titulo       

class Asignado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='usuario_asignado', help_text=gettext_lazy('Usuario de creación'))
    tarea = models.ForeignKey(Tarea, blank=False, on_delete=models.PROTECT, default=1, related_name='tarea_asignado', help_text=gettext_lazy('Usuario de creación'))
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='asignado_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='asignado_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.usuario   

class Observador(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='observador_asignado', help_text=gettext_lazy('Usuario de creación'))
    tarea = models.ForeignKey(Tarea, blank=False, on_delete=models.PROTECT, default=1, related_name='observador_asignado', help_text=gettext_lazy('Usuario de creación'))
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='observador_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='observador_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.usuario   


class Comentario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='comentario_asignado', help_text=gettext_lazy('Usuario de creación'))
    tarea = models.ForeignKey(Tarea, blank=False, on_delete=models.PROTECT, default=1, related_name='comentario_asignado', help_text=gettext_lazy('Usuario de creación'))
    descripcion = models.TextField()
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='comentario_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='comentario_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.descripcion   

class Subtarea(models.Model):
    tarea_padre = models.ForeignKey(Tarea, blank=False, on_delete=models.PROTECT, default=1, related_name='subtarea_tarea_padre', help_text=gettext_lazy('Subtarea Padre'))
    tarea_hija = models.ForeignKey(Tarea, blank=False, on_delete=models.PROTECT, default=1, related_name='subtarea_tarea_hija', help_text=gettext_lazy('Subtarea Hija'))
    
    def __str__(self):
        return self.tarea_padre   
    
class Tiempo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tiempo_asignado', help_text=gettext_lazy('Usuario de creación'))
    tarea = models.ForeignKey(Tarea, blank=False, on_delete=models.PROTECT, default=1, related_name='tiempo_asignado', help_text=gettext_lazy('Usuario de creación'))
    descripcion = models.TextField()
    tiempo= models.DecimalField(decimal_places=2 , max_digits=16 )
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tiempo_creados', help_text=gettext_lazy('Usuario de creación'))
    fecha_creacion = models.DateTimeField(blank=False, auto_now_add=True, help_text=gettext_lazy('Fecha y hora de creación'))
    usuario_modificacion = models.ForeignKey( settings.AUTH_USER_MODEL, blank=False, on_delete=models.PROTECT, default=1, related_name='tiempo_modificados', help_text=gettext_lazy('Usuario de última modificación'))
    fecha_modificacion = models.DateTimeField(blank=False, auto_now=True, help_text=gettext_lazy('Fecha y hora de última modificación'))

    def __str__(self):
        return self.descripcion       