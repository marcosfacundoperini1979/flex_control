from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def list_users(request):
    # Obtener sesiones activas
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Filtrar usuarios conectados y desconectados
    connected_users = User.objects.filter(id__in=uid_list)
    disconnected_users = User.objects.exclude(id__in=uid_list)

    return render(request, 'users/list_users.html', {
        'connected_users': connected_users,
        'disconnected_users': disconnected_users,
    })
