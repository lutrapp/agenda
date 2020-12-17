from django.urls import path, include
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/')),
#    path('', views.index),

]