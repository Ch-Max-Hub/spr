from django import forms

class ExcelUploadForm(forms.Form):
    etrap_name = forms.CharField(max_length=100)
    excel_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-file-input', 'id':'customFile'}))