from django.shortcuts import render
from .models import Agendar
from viveralegreefeliz.forms import AgendarForm


# Create your views here.
def index(request):
    return render(request,'viveralegreefeliz/index.html')

def aconselhamento(request):
    return render(request,'viveralegreefeliz/aconselhamento.html')

def agua_magnetizada_saude(request):
    return render(request,'viveralegreefeliz/agua_magnetizada_saude.html')

def agua_magnetizada(request):
    return render(request,'viveralegreefeliz/agua_magnetizada.html')

def arteterapia(request):
    return render(request,'viveralegreefeliz/arteterapia.html')

def constelacao_familiar(request):
    return render(request,'viveralegreefeliz/constelacao_familiar.html')

def galeria(request):
    return render(request,'viveralegreefeliz/galeria.html')

def introducao_constelacao_familiar(request):
    return render(request,'viveralegreefeliz/introducao_constelacao_familiar.html')

def loja(request):
    return render(request,'viveralegreefeliz/loja.html')

def mandalas(request):
    return render(request,'viveralegreefeliz/mandalas.html')

def meditacao_mentalizacao(request):
    return render(request,'viveralegreefeliz/meditacao_mentalizacao.html')

def pnl(request):
    return render(request,'viveralegreefeliz/pnl.html')

def quemsomos(request):
    return render(request,'viveralegreefeliz/quemsomos.html')

def desenvolvimento_pessoal(request):
    return render(request,'viveralegreefeliz/desenvolvimento_pessoal.html')

def terapias_integrativas(request):
    return render(request,'viveralegreefeliz/terapias_integrativas.html')

def agendar(request):
    model = Agendar
    form = AgendarForm
    template_name = 'agendar.html'

    if request.method == "POST":
        form = AgendarForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERRO FORMULARIO INVÁLIDO')
    return render(request,'viveralegreefeliz/agendar.html',{'form':form})
