from django.shortcuts import render

# Create your views here.


# query all global status and the actual user status.
#meus_status = TStatus.objects.filter(Q(user__isnull=True) | Q(user=request.user))

