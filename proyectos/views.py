from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters  
from rest_framework import generics
from .models import Estado, Sprint, Proyecto, Empresa, Tipo_tarea, Tarea, Asignado, Observador, Comentario, Subtarea
from .serializers import EstadoSerializer, SprintSerializer, ProyectoSerializer, EmpresaSerializer, Tipo_tareaSerializer, TareaSerializer, AsignadoSerializer, ObservadorSerializer, ComentarioSerializer, subtareaSerializer

# Create your views here.
class EstadoViewSet(viewsets.ModelViewSet ):
    """
    API
    Permite ver, editar y borrar Estados de las Tareas
    """

    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()


class SprintViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Sprint
    """
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Proyecto
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Empresa
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class Tipo_tareaViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Tipo_tarea
    """
    queryset = Tipo_tarea.objects.all()
    serializer_class = Tipo_tareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Tarea
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    AsignadoSerializer, ObservadorSerializer, ComentarioSerializer, subtareaSerializer

class AsignadoViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Personas Asignadas a Tarea
    """
    queryset = Asignado.objects.all()
    serializer_class = AsignadoSerializer

class ObservadorViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Observador
    """
    queryset = Observador.objects.all()
    serializer_class = ObservadorSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar Comentario
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class SubtareaViewSet(viewsets.ModelViewSet):
    """
    API
    Permite ver, editar y borrar SubTarea dependientes de otra
    """
    queryset = Subtarea.objects.all()
    serializer_class = subtareaSerializer