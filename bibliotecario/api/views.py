from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import login, logout
from .forms import FormularioLogin

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