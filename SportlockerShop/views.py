from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import Camiseta, Ropa, Sudadera, Zapatilla, Usuario, Compra
from django .views import View
from django.views.generic.detail import DetailView
from django.http import JsonResponse


# Create your views here.


class RopaListView(View):
    model1 = Camiseta
    model2 = Sudadera
    queryset = Camiseta.objects.order_by('nombre')
    queryset1 = Sudadera.objects.order_by('nombre').filter(conCapucha=True)
    queryset2 = Sudadera.objects.order_by('nombre').filter(conCapucha=False)
    template_name = 'ropa.html'

    def get(self, request):
        context = {
            'camisetas': self.queryset,
            'sudaderasConCapucha': self.queryset1,
            'sudaderasSinCapucha': self.queryset2

        }

        return render(request, 'ropa.html', context)


class ZapatillasListView(View):
    model = Zapatilla
    queryset = Zapatilla.objects.order_by('nombre')
    template_name = 'zapatillas.html'

    def get(self, request):
        context = {
            'zapatillas': self.queryset,
        }
        return render(request, 'zapatillas.html', context)


class TopVentasListView(View):
    queryset = Camiseta.objects.order_by('nombre').filter(articuloTop=True)
    queryset1 = Sudadera.objects.order_by('nombre').filter(articuloTop=True)
    queryset2 = Zapatilla.objects.order_by('nombre').filter(articuloTop=True)

    def get(self, request):
        context = {
            'topVentasCamiseta': self.queryset,
            'topVentasSudadera': self.queryset1,
            'topVentasZapatilla': self.queryset2,
        }
        return render(request, 'index.html', context)


def show_form(request):
    return render(request, 'acceso.html')


class DetalleDetailView(DetailView):
    model = Ropa
    template_name = 'detalles.html'


def detallezapatilla(request, zapatilla_id):
    zapatilla = get_object_or_404(Ropa, pk=zapatilla_id)
    context = {'zapatilla': zapatilla}
    return render(request, 'detalleszapatillas.html', context)


def post_form(request):
    contrasenya = request.POST["your_password"]
    your_email = request.POST["your_email"]
    existe=False

    usuarios = Usuario.objects.all()
    for usuario in usuarios:
        if (your_email == usuario.email):
            existe=True
            context = {
                'usuario': usuario,
            }
            if usuario.contrasenya == contrasenya:
                return render(request, 'muestraLogin.html', context)
            else:
                raise Http404("Contraseña incorrecta")


    if existe==False:
        raise Http404("No existe el email")    



def post_formRegistrar(request):
    nombre1 = request.POST["name1"]
    email1 = request.POST["email"]
    contrasenya1 = request.POST["password"]
    usuario = Usuario(nombre=nombre1, email=email1, contrasenya=contrasenya1)
    usuario.save()
    context = {
        'usuario': usuario,
    }
    return render(request, 'muestraRegistro.html', context)


def loadEmailData(request):
    usuarios = Usuario.objects.all()
    data = []
    for obj in usuarios:
        item = {
            'email': obj.email,
        }
        data.append(item)
    return JsonResponse({'data': data})
