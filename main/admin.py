from django.contrib import admin
from .models import UserEtrap, Etrap, Client

class EtrapAdmin(admin.ModelAdmin):
    list_display = ('pk', 'code', 'name', 'parent')
    list_display_links = ('code', 'name', 'parent')
    search_fields = ('code', 'name',)
    list_filter = ('parent',)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'street', 'house', 'bloc', 'room', 'service', 'old_number', 'status', 'etrap_id')
    list_display_links = ('number', 'name', 'street', 'house', 'bloc', 'room', 'service', 'old_number', 'status', 'etrap_id')
    search_fields = ('number', 'name', 'street', 'house', 'bloc', 'room', 'status', 'etrap_id__name')
    list_filter = ('service', 'status', 'etrap_id')

class UserEtrapAdmin(admin.ModelAdmin):
    list_display = ('user', 'etrap')
    list_display_links = ('user', 'etrap')
    search_fields = ('user', 'etrap')
    list_filter = ('etrap',)

admin.site.register(Etrap, EtrapAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(UserEtrap, UserEtrapAdmin)
