from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render

from .models import Client, UserEtrap, Etrap


def index(request):
    user: User = request.user
    if user.is_superuser:
        # Superuser can see all clients
        clients = Client.objects.all()
    else:
        # Operator can see clients only from their etrap
        try:
            _user = UserEtrap.objects.get(user=user)
            clients = Client.objects.filter(Q(etrap=_user.etrap) | Q(etrap__parent=_user.etrap))
        except UserEtrap.DoesNotExist:
            clients = []
    context = {
        'title': '09',
        'user': user,
        'clients': clients,
    }
    return render(request, 'index.html', context=context)


def etraps(request):
    context = {
        'title': '09 | Etraplar',
    }
    return render(request, 'index.html', context=context)


def users(request):
    context = {
        'title': '09 | Ulanyjylar',
    }
    return render(request, 'index.html', context=context)


def add_info(request):
    context = {
        'title': '09 | Maglumat goş',
    }
    return render(request, 'index.html', context=context)


def add_info_file(request):
    context = {
        'title': '09 | Maglumat file ýükle',
    }
    return render(request, 'index.html', context=context)


def dark_mode(request, turn_on):
    if turn_on == 0: request.session['dark_mode'] = False
    if turn_on == 1: request.session['dark_mode'] = True
    return render(request, 'index.html')