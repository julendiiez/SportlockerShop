from django.shortcuts import render
from .models import Camiseta,Ropa,Sudadera,Zapatilla,Usuario,Compra
from django .views import View


# Create your views here.
def index(request):
    return render(request,'index.html')

class CamisetaListView(View):
    model=Camiseta
    queryset=Camiseta.objects.order_by('nombre')
    template_name='ropa.html'

    def get(self,request):
        context={
            'camisetas':self.queryset
        }
        return render(request,'ropa.html',context)