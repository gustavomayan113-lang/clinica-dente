from django.urls import path

from . import views

app_name = "clinica"

urlpatterns = [
    path("", views.home, name="home"),
    path("servicos/", views.servicos, name="servicos"),
    path("servicos/<slug:slug>/", views.servico_detalhe, name="servico_detalhe"),
    path("equipe/", views.equipe, name="equipe"),
    path("contato/", views.contato, name="contato"),
]