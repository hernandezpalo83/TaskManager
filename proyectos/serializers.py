from rest_framework.serializers import ModelSerializer
from .models import Estado, Sprint, Proyecto, Empresa, Tipo_tarea, Tarea, Asignado, Observador, Comentario, Subtarea



class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class SprintSerializer(ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

class ProyectoSerializer(ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class Tipo_tareaSerializer(ModelSerializer):
    class Meta:
        model = Tipo_tarea
        fields = '__all__'

class TareaSerializer(ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class AsignadoSerializer(ModelSerializer):
    class Meta:
        model = Asignado
        fields = '__all__'

class ObservadorSerializer(ModelSerializer):
    class Meta:
        model = Observador
        fields = '__all__'

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class subtareaSerializer(ModelSerializer):
    class Meta:
        model = Subtarea
        fields = '__all__'
