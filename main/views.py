from django.shortcuts import render

from .models import Client, CustomUser, Etrap


def index(request):
    user: CustomUser = request.user
    if user.is_superuser:
        # Superuser can see all clients
        clients = Client.objects.all()
    # elif user.groups.filter(name='Admin').exists():
    else:
        # Operator can see clients only from their etrap
        clients = Client.objects.filter(etrap=user.etrap)
    print(user)
    print(clients[0])
    context = {
        'title': '09',
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