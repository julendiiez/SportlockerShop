from django.shortcuts import render
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

def post_form(request):
    model=Usuario
    email1=request.POST["your_email"]
    queryset=Usuario.objects.filter(email=email1)
    contraseña=request.POST["your_password"]

