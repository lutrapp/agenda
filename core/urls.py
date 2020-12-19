from django.urls import path, include
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/agenda/')),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

    #    path('', views.index),

]