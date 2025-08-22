from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def index(request):
    return render(request, 'biografia/index.html', {})


def list_biographies(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        pessoas = Pessoa.objects.filter(biografia__icontains=pesquisa)
    else:
        pessoas = Pessoa.objects.all()
    
    context = {
        'pessoas': pessoas,
    }
    return render(request, 'biografia/lista.html', context)


def detail_biography(request, pessoa_id):
    try:
        pessoa = Pessoa.objects.get(id=pessoa_id)
    except Pessoa.DoesNotExist:
        pessoa = None
    
    context = {
        'pessoa': pessoa,
    }
    return render(request, 'biografia/detalhe.html', context)