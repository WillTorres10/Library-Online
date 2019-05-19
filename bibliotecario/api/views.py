from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.views import login, logout
from django.http import JsonResponse
import requests, json

IP_estudante = 'http://nginx/estudante'
IP_livro = 'http://nginx/livro'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginView(request, *args, **kwargs):

    if request.user.is_authenticated:
        return redirect('api:inicio')

    kwargs['extra_context'] = {'next': reverse('api:acessar')}
    kwargs['template_name'] = 'login.html'
    return login(request, *args, **kwargs)

def logoutView(request, *args, **kwargs):
    kwargs['next_page'] = reverse('api:acessar')
    return logout(request, *args, **kwargs)

'''
    Estudantes
'''

def cadastrarEstudante(request):
    if request.GET is not None:
        return render(request, 'estudante/cadastrar.html')

def pesquisarEstudante(request):
    if request.method == 'GET':
        return render(request, 'estudante/pesquisar.html')
    elif request.method == 'POST':
        matricula = request.POST['matricula']
        session = requests.Session()
        session.trust_env = False
        lista = requests.post(IP_estudante+'/api/buscarEstudante/', data={'matricula': matricula})
        if lista.json()['dados'] != -1:
            template = render_to_string('estudante/listar/pesquisa.html', {'estudantes': lista.json()['dados']})
            return JsonResponse({'retorno': template})
        else:
            return JsonResponse({'retorno': 'Não foi possível encontrar'})

def removerEstudante(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        lista = requests.post(IP_estudante + '/api/removerEstudante/', data={'matricula': matricula})
        if lista.json()['deletado']:
            return JsonResponse({'status':'success', 'mensagem':'Estudante removido com sucesso'})
        else:
            return JsonResponse({'status': 'danger', 'mensagem': 'Erro ao remover estudante'})

'''
    Livros
'''

def emprestarLivro(request):
    if request.method == 'GET':
        return render(request, 'livros/emprestar.html')
    elif request.method == 'POST':
        codigo = request.POST['codigo']
        lista = requests.post(IP_livro + '/api/buscarLivroNome/', data={'codigo': codigo})
        if lista.json()['dados'] != -1:
            template = render_to_string('livros/listar/pesquisaEmprestar.html', {'livros': lista.json()['dados']})
            return JsonResponse({'retorno': template})
        else:
            return JsonResponse({'retorno': 'Não foi possível encontrar'})

def emprestandoLivro(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        return JsonResponse({'retorno': render_to_string('livros/emprestando.html', {'codigo': codigo})})

def finalizarEmprestimo(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        matricula = request.POST['matriculaT']
        if matricula != "":
            verificarEstudante = requests.post(IP_estudante + '/api/verificaEstudante/', data={'matricula': matricula})
            if verificarEstudante.json()['status'] == 1:
                lista = requests.post(IP_livro + '/api/emprestarLivro/', data={'codigo': codigo, 'matricula': matricula})
                if lista.json()['status'] == 1:
                    return JsonResponse({'status': 'success', 'mensagem': 'Livro emprestado com sucesso!'})
            else:
                return JsonResponse({'status': 'danger', 'mensagem': 'Estudante Não Existe'})
        else:
            return JsonResponse({'status': 'danger', 'mensagem': 'Preencha todos os campos!'})


def receberLivro(request):
    if request.method == 'GET':
        return render(request, 'livros/receber.html')
    elif request.method == 'POST':
        matricula = request.POST['matricula']
        lista = requests.post(IP_estudante + '/api/buscarEstudante/', data={'matricula': matricula})
        if lista.json()['dados'] != -1:
            template = render_to_string('livros/listar/estudante.html', {'estudantes': lista.json()['dados']})
            return JsonResponse({'retorno': template})
        else:
            return JsonResponse({'retorno': 'Não foi possível encontrar'})

def cadastrarLivro(request):
    return render(request, 'livros/cadastrar.html')

def removerLivro(request):
    if request.method == 'GET':
        return render(request, 'livros/remover.html')
    elif request.method == 'POST':
        codigo = request.POST['codigo']
        lista = requests.post(IP_livro + '/api/buscarLivro/', data={'codigo': codigo})
        if lista.json()['dados'] != -1:
            template = render_to_string('livros/listar/pesquisa.html', {'livros': lista.json()['dados']})
            return JsonResponse({'retorno': template})
        else:
            return JsonResponse({'retorno': 'Não foi possível encontrar'})

def removendoLivro(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        lista = requests.post(IP_livro + '/api/removerLivro/', data={'codigo': codigo})
        if lista.json()['deletado']:
            return JsonResponse({'status':'success', 'mensagem':'Livro removido com sucesso'})
        else:
            return JsonResponse({'status': 'danger', 'mensagem': 'Erro ao remover livro'})

def listarHistorico(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        Estudante = requests.post(IP_estudante+'/api/buscarEstudante/', data={'matricula': matricula})
        dados = Estudante.json()['dados'][0]
        nomeEstudante = dados['first_name'] + ' ' + dados['last_name']
        historico = requests.post(IP_livro + '/api/historicoEmprestimos/', data={'matricula': matricula})
        if historico.json()['status'] == 1:
            templateHistorico = render_to_string('livros/listar/alugados.html', {'livros': historico.json()['conteudo']})
            return JsonResponse({'nomeEstudante': nomeEstudante, 'conteudo': templateHistorico})
        else:
            return JsonResponse({'nomeEstudante': nomeEstudante, 'conteudo': "Não há nada nos registros"})

def confirmandoEntregaEmprestimo(request):
    if request.method == 'POST':
        idEmprestimo = request.POST['idEmprestimo']
        confirmando = requests.post(IP_livro + '/api/confirmandoRecebimentoEmprestimo/', data={'idEmprestimo': idEmprestimo})
        print(confirmando)
        if confirmando.json()['status'] == 1:
            return JsonResponse({'status': 'success', 'mensagem': 'Confirmação realizada com sucesso!'})
        else:
            return JsonResponse({'status': 'danger', 'mensagem': 'Erro na confirmação da entrega, tente novamente!'})
