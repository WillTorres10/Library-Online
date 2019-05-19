from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name="inicio"),
    path('gerarCSRF/', views.gerarCSRF, name="gerarCSRF"),
    path('criando/', views.cadastrarLivro, name="criando"),
    path('buscarLivro/', views.procurarLivro, name="procurando"),
    path('buscarLivroNome/', views.procurarLivroNome, name="procurandoNome"),
    path('removerLivro/', views.removerLivro, name="removendo"),
    path('emprestarLivro/', views.emprestarLivro, name="emprestando"),
    path('historicoEmprestimos/', views.historicoEmprestimo, name="recebendo"),
    path('confirmandoRecebimentoEmprestimo/', views.confirmandoRecebimentoEmprestimo, name="confirmandoRecebimentoEmprestimo")
]