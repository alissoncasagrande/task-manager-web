from django.contrib import admin
from .models        import Task, TStatus
from django.db      import models

# Register your models here.
# admin.site.register(TStatus)
# admin.site.register(Task)

@admin.register(TStatus)
class TStatusAdmin(admin.ModelAdmin):
    list_display = ('description', 'user')

    # 1. Filtra o que aparece na listagem do Admin
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return [f for f in qs if qs != 'user']
        return qs

    # 2. Salva automaticamente o usuário logado ao criar um novo status
    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user

        super().save_model(request, obj, form, change)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'created_at')
    list_filter = ('status', 'user')

    # Filtra as Tasks para o usuário só ver as dele
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
