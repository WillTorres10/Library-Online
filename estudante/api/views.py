from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from .serialization import *
import requests, json
from django.template.loader import render_to_string

IP_livro = "http://nginx/livro"

def index(request):
    if request.method == "GET":
        usuario = Estudante.objects.get(id = request.user.id)
        return render(request, 'index.html', {'matricula': usuario.matricula})

def loginView(request, *args, **kwargs):

    if request.user.is_authenticated:
        return redirect('api:inicio')

    kwargs['extra_context'] = {'next': reverse('api:acessar')}
    kwargs['template_name'] = 'login.html'
    return login(request, *args, **kwargs)

def logoutView(request, *args, **kwargs):
    kwargs['next_page'] = reverse('api:acessar')
    return logout(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def cadastrarEstudante(request):
    if request.method == 'POST':
        if request.POST['senha'] == request.POST['repetirSenha']:
            if Estudante.objects.all().filter(matricula=request.POST['matricula']).count() == 0:
                if Estudante.objects.all().filter(email=request.POST['email']).count() == 0:
                    if Estudante.objects.all().filter(username=request.POST['username']).count() == 0:
                        user = Estudante()
                        user.email = request.POST['email']
                        user.username = request.POST['username']
                        user.first_name = request.POST['primeiroNome']
                        user.last_name = request.POST['ultimoNome']
                        user.set_password(request.POST['senha'])
                        user.matricula = request.POST['matricula']
                        user.save()
                        return Response({'status': 'success', 'mensagem': 'Usuário cadastrado com sucesso!'})
                    else:
                        return Response({'status': 'danger', 'mensagem': 'Username já está cadastrado'})
                else:
                    return Response({'status': 'danger', 'mensagem': 'Email já cadastrado no sistema'})
            else:
                return Response({'status': 'danger', 'mensagem': 'Matrícula já cadastrada no sistema'})
        else:
            return Response({'status':'danger', 'mensagem':'Senhas não combinam'})
    else:
        return HttpResponse("Nada")

@api_view(['GET'])
def gerarCSRF(request):
    if request.method == 'GET':
        return JsonResponse({'csrf': get_token(request)})


@csrf_exempt
def buscarEstudante(request):
    if request.method == 'GET':
        return HttpResponse('Estudante')
    elif request.method == 'POST':
        matricula = request.POST.get('matricula')
        if matricula is not None:
            normal = Estudante.objects.filter(matricula__contains=matricula)
            if normal:
                serializado = EstudanteSerializer(normal, many=True)
                return JsonResponse({'dados': serializado.data})
            else:
                return JsonResponse({'dados': -1})

@api_view(['POST'])
@csrf_exempt
def removerEstudante(request):
    matricula = request.POST['matricula']
    Estudante.objects.get(matricula=matricula).delete()
    return Response({'deletado':True})

@api_view(['POST'])
@csrf_exempt
def verfificaEstudante(request):
    matricula = request.POST['matricula']
    estudante = Estudante.objects.filter(matricula=matricula)
    if estudante:
        return Response({'status': 1, 'dados': EstudanteSerializer(estudante, many=True).data})
    else:
        return Response({'status': -1})

def listarHistorico(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        estudante = Estudante.objects.filter(matricula=matricula)
        nomeEstudante = estudante[0].first_name + ' ' + estudante[0].last_name
        historico = requests.post(IP_livro + '/api/historicoEmprestimos/', data={'matricula': matricula})
        if historico.json()['status'] == 1:
            templateHistorico = render_to_string('alugados.html', {'livros': historico.json()['conteudo']})
            return JsonResponse({'nomeEstudante': nomeEstudante, 'conteudo': templateHistorico})
        else:
            return JsonResponse({'nomeEstudante': nomeEstudante, 'conteudo': "Não há nada nos registros"})

def buscarLivro(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        lista = requests.post(IP_livro + '/api/buscarLivroNome/', data={'codigo': codigo})
        if lista.json()['dados'] != -1:
            template = render_to_string('livros/resultadoPesquisaLivro.html', {'livros': lista.json()['dados']})
            return JsonResponse({'retorno': template})
        else:
            return JsonResponse({'retorno': 'Não foi possível encontrar'})