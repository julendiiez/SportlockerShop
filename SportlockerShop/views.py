from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Camiseta,Ropa,Sudadera,Zapatilla,Usuario,Compra
from django .views import View


# Create your views here.


class RopaListView(View):
    model1=Camiseta
    model2=Sudadera
    queryset=Camiseta.objects.order_by('nombre')
    queryset1=Sudadera.objects.order_by('nombre').filter(conCapucha=True)
    queryset2=Sudadera.objects.order_by('nombre').filter(conCapucha=False)
    template_name='ropa.html'

    def get(self,request):
        context={
            'camisetas':self.queryset,
            'sudaderasConCapucha':self.queryset1,
            'sudaderasSinCapucha':self.queryset2

        }
        
        return render(request,'ropa.html',context)
class ZapatillasListView(View):
    model=Zapatilla
    queryset=Zapatilla.objects.order_by('nombre')
    template_name='zapatillas.html'
    def get(self,request):
        context={
            'zapatillas':self.queryset,
        }
        return render(request,'zapatillas.html',context)

class TopVentasListView(View):
    model=Ropa
    queryset=Ropa.objects.order_by('nombre').filter(articuloTop=True)
    template_name='zapatillas.html'
    def get(self,request):
        context={
            'topVentas':self.queryset,
        }
        return render(request,'index.html',context)

def show_form(request):
  return render(request,'acceso.html')

def post_form(self,request):
    model=Usuario
    email1=request.POST["your_email"]
    queryset=Usuario.objects.filter(email=email1)
    context={
        'usuario':self.queryset,    
    }
    return render(request,'muestraLogin.html',context)
    contraseña=request.POST["your_password"]

    
   # else:
    #    return render(request,'acceso.html')
def detalle(request,ropa_id):
    ropa=get_object_or_404(Ropa,pk=ropa_id)
    context={'ropa':ropa}
    return render (request,'detalles.html',context)

def detallezapatilla(request,zapatilla_id):
    zapatilla=get_object_or_404(Ropa,pk=zapatilla_id)
    context={'zapatilla':zapatilla}
    return render (request,'detalleszapatillas.html',context)

