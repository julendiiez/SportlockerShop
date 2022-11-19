from django.contrib import admin
from .models import Usuario, Ropa, Compra,Zapatilla
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ropa)
admin.site.register(Compra)
admin.site.register(Zapatilla)