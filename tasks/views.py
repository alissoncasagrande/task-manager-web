from django.shortcuts               import render
from django.contrib.auth.decorators import login_required
from django.db.models               import Q
from .models                        import Task   
from .models                        import TStatus


# Create your views here.
# query all global status and the actual user status.
#meus_status = TStatus.objects.filter(Q(user__isnull=True) | Q(user=request.user))

#from django.shortcuts import render


@login_required # Garante que só quem está logado acessa essa página
def task_list(request):
    # Buscamos apenas as tarefas do usuário que fez o request
    query = Q(user=request.user)
    tasks = Task.objects.filter(query).order_by('-created_at')
    #tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    
    # Enviamos os dados para o template HTML
    return render(request, 'tasks/task_list.html', {'tasks': tasks})