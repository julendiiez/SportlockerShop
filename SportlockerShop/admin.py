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
     list_display=('id','usuario','fechaDeCompra')
     list_filter=('fechaDeCompra',)

@admin.register(Zapatilla)
class ZapatillaAdmin(admin.ModelAdmin):
    list_display=('id','nombre','precio','cantidad',)
    search_fields=('nombre',)
    ordering=('cantidad',)
@admin.register(Sudadera)
class SudaderaAdmin(admin.ModelAdmin):
    list_display=('id','nombre','precio','cantidad',)
    search_fields=('nombre',)
    ordering=('cantidad',)

@admin.register(Camiseta)
class CamisetaAdmin(admin.ModelAdmin):
    list_display=('id','nombre','precio','cantidad',)
    search_fields=('nombre',)
    ordering=('cantidad',)



