from django.shortcuts import render
from django.http import Http404
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
    contrasenya=request.POST["your_password"]
    your_email=request.POST["your_email"]
    try:
        usuario=Usuario.objects.get(email=your_email)
        context={
            'usuario':usuario,
        }
    except:
        raise Http404('No existe el email')
    if usuario.contrasenya==contrasenya:
        return render(request,'muestraLogin.html',context)
    else:
        raise Http404("Contraseña incorrecta")
    
def post_formRegistrar(request):
    nombre1=request.POST["name"]
    email1=request.POST["email"]
    contrasenya1=request.POST["password"]
    repetirContrasenya1=request.POST["repeatpassword"]
    if contrasenya1==repetirContrasenya1:
        usuario=Usuario(nombre=nombre1,email=email1,contrasenya=contrasenya1)
        usuario.save()
        context={
            'usuario':usuario,
        }
        return render(request,'muestraRegistro.html',context)
    else:
        raise Http404("La contraseña no coincide")