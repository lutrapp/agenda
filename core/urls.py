from django.urls import path, include
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

    #    path('', views.index),

]