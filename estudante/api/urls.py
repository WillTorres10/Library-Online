from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'api'

urlpatterns = [
    path('', login_required(views.index), name="inicio"),
    path('acessar/', views.loginView, name='acessar'),
    path('sair/', views.logoutView, name='sair')
]