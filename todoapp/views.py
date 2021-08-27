from django.shortcuts import render
from .models import Tarefas
from .forms import TarefaForm


# Create your views here.
def index(request):
    tarefa_adicionada = Tarefas.objects.all()
    context = {'tarefa_adicionada': tarefa_adicionada}
    return render(request, 'todoapp/index.html', context)


def adicionar(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TarefaForm()

    return render(request, 'todoapp/adicionar.html', {'form': form})
