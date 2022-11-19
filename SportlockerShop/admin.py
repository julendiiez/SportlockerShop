from django.contrib import admin
from .models import Usuario,Compra,Zapatilla,Sudadera,Camiseta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Compra)
admin.site.register(Zapatilla)
admin.site.register(Sudadera)
admin.site.register(Camiseta)

