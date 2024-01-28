from django.contrib import admin
from .models import Estado, Sprint, Proyecto, Empresa, Tipo_tarea, Tarea, Asignado, Observador, Comentario, Subtarea, Tiempo

admin.site.site_header = "TaskManager"
admin.site.index_title = "Panel de control TaskManager"
admin.site.site_title = "TaskManager"

# Register your models here.
admin.site.register( Estado )
admin.site.register( Sprint )
admin.site.register( Proyecto )
admin.site.register( Empresa )
admin.site.register( Tipo_tarea )
admin.site.register( Asignado )
admin.site.register( Observador )
admin.site.register( Comentario )
admin.site.register( Subtarea )
admin.site.register( Tiempo )


class TareaAdmin(admin.ModelAdmin):
    # lista
    list_display = (
        "titulo", 
        "tiempo_estimado",
        "estado",
        "proyecto",
        "tipo"
        )
    list_filter = ("proyecto", "estado", "tipo")    
    search_fields = ("titulo",)
    # formulario
    fields = (
        "empresa",
        "proyecto",
        "tipo",
        "titulo", 
        "descripcion", 
        "fechaini",
        "fechafin",
        "tiempo_estimado",
        "coste",
        "estado",
        "sprint",
        )

admin.site.register( Tarea , TareaAdmin)