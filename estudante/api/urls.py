from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'api'

urlpatterns = [
    path('', login_required(views.index), name="inicio"),
    path('acessar/', views.loginView, name="acessar"),
    path('sair/', login_required(views.logoutView), name="sair"),
    path('criando/', views.cadastrarEstudante, name="criando"),
    path('gerarCSRF/', views.gerarCSRF, name="gerarCSRF"),
    path('buscarEstudante/', views.buscarEstudante, name="buscarEstudante"),
    path('removerEstudante/', views.removerEstudante, name="removerEstudante"),
    path('verificaEstudante/', views.verfificaEstudante, name="verificandoEstudante"),
    path('listandoHistorico/', login_required(views.listarHistorico), name="listandoHistorico"),
    path('buscarLivro/', login_required(views.buscarLivro), name="buscandoHistorico")
]