'''
models.py
DJango definition of models for task-manager-web

author: Alisson Casagrande
License: 

'''

from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuários do Django

class TStatus(models.Model):
    # Definimos o status (Ex: Pendente, Em Andamento, Concluído)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    # Relacionamento com o Status
    status = models.ForeignKey(TStatus, on_delete=models.PROTECT)
    
    # Relacionamento com o Usuário (Dono da tarefa)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Campos de controle temporal (seus favoritos de DBA)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

