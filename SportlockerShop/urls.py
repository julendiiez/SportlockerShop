from django.urls import path

from. import views
from SportlockerShop.views import RopaListView,ZapatillasListView,TopVentasListView


urlpatterns = [
    path('',TopVentasListView.as_view()),
    path('ropa/',RopaListView.as_view()),
    path('zapatillas/',ZapatillasListView.as_view()),
    path('acceso/',views.show_form,name='registro'),


]