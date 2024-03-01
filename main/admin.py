from django.contrib import admin
from .models import CustomUser, Etrap, Client

class EtrapAdmin(admin.ModelAdmin):
    list_display = ('pk', 'etrap_code', 'etrap_name', 'parent')
    list_display_links = ('etrap_code', 'etrap_name', 'parent')
    search_fields = ('etrap_code', 'etrap_name',)
    list_filter = ('parent',)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'name', 'street', 'house', 'bloc', 'room', 'service', 'old_number', 'status', 'etrap_id')
    list_display_links = ('number', 'name', 'street', 'house', 'bloc', 'room', 'service', 'old_number', 'status', 'etrap_id')
    search_fields = ('number', 'name', 'street', 'house', 'bloc', 'room', 'status', 'etrap_id__etrap_name')
    list_filter = ('service', 'status', 'etrap_id')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'etrap')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email', 'etrap__etrap_name')
    list_filter = ('etrap',)

admin.site.register(Etrap, EtrapAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
