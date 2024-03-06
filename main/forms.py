from django import forms

from .models import Etrap

class ExcelUploadForm(forms.Form):
    etrap_name = forms.CharField(max_length=100)
    excel_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-file-input', 'id':'customFile'}))

class ClientAddForm(forms.Form):
    etrap_name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100, required=False)
    house = forms.CharField(max_length=100, required=False)
    bloc = forms.CharField(max_length=100, required=False)
    room = forms.CharField(max_length=100, required=False)
    service = forms.IntegerField(required=False)
    old_number = forms.CharField(max_length=100, required=False)
    status = forms.CharField(max_length=100, required=False)