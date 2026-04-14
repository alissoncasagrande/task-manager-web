'''
models.py
DJango definition of models for task-manager-web

author: Alisson Casagrande
License: 

'''

from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuários do Django

class TStatus(models.Model):
    # Task Status like ToDo, In-progress, Done
    description = models.CharField(max_length=50)
    # It will be null when its a global status, or it can be a user created status.
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    class Meta: # how the admin web page will show the TStatus Class
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        if (self.user): 
            return f"{self.description} (Private: {self.user.username})"
        return f"{self.description} (System)"

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    
    # FK (id) Status
    status = models.ForeignKey(TStatus, on_delete=models.PROTECT)
    
    # FK (id) User (Owner of the Task)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Time control fields (updated will be same as created when its new)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

