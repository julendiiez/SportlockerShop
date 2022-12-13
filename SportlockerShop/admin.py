from django.contrib import admin
from .models import Usuario,Compra,Zapatilla,Sudadera,Camiseta
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id','nombre')
    search_fields=('nombre',)
    ordering=('id',)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
     list_display=('id','fechaDeCompra')

admin.site.register(Zapatilla)
admin.site.register(Sudadera)
admin.site.register(Camiseta)

