from django.urls import path

from. import views
from SportlockerShop.views import RopaListView,ZapatillasListView,TopVentasListView,DetalleDetailView,loadEmailData


urlpatterns = [
    path('',TopVentasListView.as_view()),
    path('ropa/',RopaListView.as_view()),
    path('zapatillas/',ZapatillasListView.as_view()),
    path('acceso/',views.show_form,name='registro'),
    path('accesoCorrecto/',views.post_form,name="correcto"),
    path('ropa/<pk>/',DetalleDetailView.as_view(),name='vista_detalle'),
    path('zapatillas/<int:zapatilla_id>',views.detallezapatilla,name='vista_detalle_zapatilla'),
    path('registroCorrecto/',views.post_formRegistrar,name="registroCorrecto"),
    path('informacionEmails',views.loadEmailData,name="email")
    ]