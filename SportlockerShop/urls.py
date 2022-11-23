from django.urls import path

from. import views
from SportlockerShop.views import RopaListView,ZapatillasListView,TopVentasListView


urlpatterns = [
    path('',TopVentasListView.as_view()),
    path('ropa/',RopaListView.as_view()),
    path('zapatillas/',ZapatillasListView.as_view()),
    path('acceso/',views.show_form,name='iniciar'),
    path('accesoCorrecto/',views.post_form,name="correcto"),
    path('registroCorrecto/',views.post_formRegistrar,name='registro'),


]