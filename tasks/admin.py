from django.contrib import admin
from .models import Task, TStatus

# Register your models here.
admin.site.register(TStatus)
admin.site.register(Task)

