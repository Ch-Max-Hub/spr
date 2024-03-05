from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
import pandas as pd

from .forms import ExcelUploadForm
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
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_data = request.FILES['excel_file']
            df = pd.read_excel(excel_data)  # Parse Excel file using pandas
            for index, row in df.iterrows():
                Client.objects.create(
                    number=row['Number'],
                    name=row['Name'],
                    street=row['Street'],
                    house=row['House'],
                    # Add more fields as needed
                )
            return render(request, 'upload_form.html')
    else:
        form = ExcelUploadForm()

    context = {
        'title': '09 | Maglumat file ýükle',
        'form': form,
    }
    return render(request, 'upload_form.html', context=context)


def dark_mode(request, turn_on):
    if turn_on == 0: request.session['dark_mode'] = False
    if turn_on == 1: request.session['dark_mode'] = True
    return render(request, 'index.html')