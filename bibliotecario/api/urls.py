from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'api'

urlpatterns = [
    path('', login_required(views.index), name="inicio"),
    path('acessar/', views.loginView, name='acessar'),
    path('sair/', login_required(views.logoutView), name='sair'),

    path('cadastrar/estudante/', login_required(views.cadastrarEstudante), name="cadastrarEstudante"),
    path('pesquisar/estudante/', login_required(views.pesquisarEstudante), name="pesquisarEstudante"),
    path('remover/estudante/', login_required(views.removerEstudante), name="removerEstudante"),

    path('emprestar/livro/', login_required(views.emprestarLivro), name="emprestarLivro"),
    path('emprestandoLivro', login_required(views.emprestandoLivro), name="emprestandoLivro"),
    path('emprestar/livro/realizar/', login_required(views.finalizarEmprestimo), name="emprestandoLivroFinalizar"),
    path('cadastrar/livro/', login_required(views.cadastrarLivro), name="cadastrarLivro"),
    path('receber/livro/', login_required(views.receberLivro), name="receberLivro"),
    path('remover/livro/', login_required(views.removerLivro), name="removerLivro"),
    path('removendoLivro/', login_required(views.removendoLivro), name="removendoLivro"),
    path('listarHistorico', login_required(views.listarHistorico), name="listarHistorico"),
    path('confirmandoEntregaEmprestimo/', login_required(views.confirmandoEntregaEmprestimo), name='confirmandoEntrega'),

]