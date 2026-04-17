from django.urls    import path
from .              import views

urlpatterns = [
    # entry point for tasks app (task_list)
    path('', views.task_list, name='task_list'),
]