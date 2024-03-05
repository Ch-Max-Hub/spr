from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseNotAllowed
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
        # Operator can see clients only from their etrap and sub etraps
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

def add_info_file(request):
    user = request.user
    if user.is_superuser:
        # Superuser can see all clients
        etr = Etrap.objects.all()
    elif user.groups.filter(name='Admin').exists():
        # Admins can see only their etrap and sub etraps
        try:
            _user = UserEtrap.objects.get(user=user)
            etr = Etrap.objects.filter(Q(pk=_user.etrap.pk) | Q(parent=_user.etrap))
        except UserEtrap.DoesNotExist:
            etr = []
    else:
        return HttpResponseNotAllowed(['POST'])

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            etrap_name = request.POST.get('etrap_name')
            excel_data = request.FILES.get('excel_file')
            if etrap_name and excel_data:
                df = pd.read_excel(excel_data)  # Parse Excel file using pandas
                for index, row in df.iterrows():
                    data = {'etrap': Etrap.objects.get(name=etrap_name)}
                    if row.get('Number', ''): data.update({'number': str(row['Number']).strip()})
                    if row.get('Name', ''): data.update({'name': str(row['Name']).strip()})
                    if row.get('Street', ''): data.update({'street': str(row['Street']).strip()})
                    if row.get('House', ''): data.update({'house': str(row['House']).strip()})
                    if row.get('Bloc', ''): data.update({'bloc': str(row['Bloc']).strip()})
                    if row.get('Room', ''): data.update({'room': str(row['Room']).strip()})
                    if row.get('Service', ''): data.update({'service': int(row['Service'])})
                    if row.get('Old number', ''): data.update({'old_number': str(row['Old number']).strip()})
                    if row.get('Status', ''): data.update({'status': str(row['Status']).strip()})
                    try: Client.objects.create(**data)
                    except Exception as e: print(e)
                form = ExcelUploadForm()
    else:
        form = ExcelUploadForm()

    context = {
        'title': '09 | Maglumat file ýükle',
        'etraps': etr,
        'form': form,
    }
    return render(request, 'upload_form.html', context=context)

def dark_mode(request, turn_on):
    if turn_on == 0: request.session['dark_mode'] = False
    if turn_on == 1: request.session['dark_mode'] = True
    return render(request, 'index.html')