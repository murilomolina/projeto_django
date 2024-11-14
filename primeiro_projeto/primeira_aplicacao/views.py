from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# GET
def index(request):
    variaveis = { # esse dicionario pode ser populado com qualquer tipo de dados, seja requisição, banco de dados....
        'nome': 'Murilo',
    }
    return render(request, 'primeira_aplicacao/index.html', variaveis)
    # return HttpResponse('Hello, Django')