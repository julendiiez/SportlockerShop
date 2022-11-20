from django.urls import path

from. import views
from SportlockerShop.views import CamisetaListView


urlpatterns = [
    path('',views.index,name='index'),
    path('ropa/',CamisetaListView.as_view()),


]