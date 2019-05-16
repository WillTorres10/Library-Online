from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import *
from .serialization import *

def index(request):
    return HttpResponse('TESTE')

@api_view(['GET'])
def gerarCSRF(request):
    if request.method == 'GET':
        return JsonResponse({'csrf': get_token(request)})

@api_view(['GET', 'POST'])
def cadastrarLivro(request):
    if request.method == 'POST':
        if Livro.objects.filter(codigo=request.POST['codigo']).count() == 0:
            livro = Livro()
            livro.autor = request.POST['autor']
            livro.codigo = request.POST['codigo']
            livro.titulo = request.POST['titulo']
            livro.versao = request.POST['versao']
            livro.volume = request.POST['volume']
            livro.save()
            return Response({'status': 'success', 'mensagem': 'Livro cadastrado com sucesso!'})
        else:
            return Response({'status': 'danger', 'mensagem': 'Matrícula já existe'})

@api_view(['POST'])
def procurarLivro(request):
    if request.method == 'POST':
        if request.POST['codigo'] is not None:
            codigo = request.POST['codigo']
            normal = Livro.objects.filter(codigo__contains=codigo)
            if normal:
                serializado = LivroSerializer(normal, many=True)
                return Response({'dados': serializado.data})
            else:
                return Response({'dados': -1})

@api_view(['POST'])
def procurarLivroNome(request):
    if request.method == 'POST':
        if request.POST['codigo'] is not None:
            codigo = request.POST['codigo']
            normal = Livro.objects.filter(titulo__contains=codigo)
            if normal:
                serializado = LivroSerializer(normal, many=True)
                return Response({'dados': serializado.data})
            else:
                return Response({'dados': -1})

@api_view(['POST'])
def removerLivro(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        Livro.objects.get(codigo=codigo).delete()
        return Response({'deletado':True})

@api_view(['POST'])
def emprestarLivro(request):
    if request.method == 'POST':
        emprestimo = EmprestarLivro()
        emprestimo.alugado = 1
        emprestimo.codigoLivro = Livro.objects.get(codigo=request.POST['codigo'])
        emprestimo.matriculaLivro = request.POST['matricula']
        emprestimo.save()
        return Response({'status': 1})

@api_view(['POST'])
def historicoEmprestimo(request):
    if request.method == 'POST':
        matriculaEstudante = request.POST['matricula']
        busca = EmprestarLivro.objects.filter(matriculaLivro=matriculaEstudante)
        if busca.count() > 0:
            retornar = []
            for aluga in busca:
                dadosLivro = {
                    'titulo': aluga.codigoLivro.titulo,
                    'codigo': aluga.codigoLivro.codigo,
                    'status': aluga.alugado,
                    'id': aluga.id
                }
                retornar.append(dadosLivro)
            return Response({'status': 1, 'conteudo': retornar})
        else:
            return Response({'status': -1})

@api_view(['POST'])
def confirmandoRecebimentoEmprestimo(request):
    if request.method == 'POST':
        idEmprestimo = request.POST['idEmprestimo']
        emprestimo = EmprestarLivro.objects.get(id=idEmprestimo)
        emprestimo.alugado = 0
        emprestimo.save()
        return Response({'status': 1})