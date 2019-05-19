from django import forms
from django.db import models

class FormularioLogin(forms.Form):
    username = forms.CharField(required=True, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuário', 'class': 'form-control'}))
    password = forms.CharField(required=True, label='',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Senha', 'class': 'form-control'}))