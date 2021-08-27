# import Forms
from django import forms
from .models import Tarefas


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ('tarefa_texto', 'descricao_texto', 'importancia')
