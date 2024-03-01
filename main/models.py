from django.contrib.auth.models import AbstractUser
from django.db import models


class Etrap(models.Model):
    etrap_code = models.IntegerField('Etrap kod')
    etrap_name = models.CharField('Ady', max_length=100)
    parent = models.ForeignKey('self', verbose_name='Degişli etraby', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        unique_together = ['etrap_name', 'parent']
        verbose_name = 'Etrap'
        verbose_name_plural = 'Etraplar'

    def __str__(self):
        return self.etrap_name
    
    def save(self, *args, **kwargs):
        if self.parent:
            self.etrap_code = self.parent.etrap_code
        super().save(*args, **kwargs)


class CustomUser(AbstractUser):
    etrap = models.ForeignKey(Etrap, on_delete=models.SET_NULL, null=True, blank=True)


class Client(models.Model):
    number = models.CharField('Nomer', max_length=20)
    name = models.CharField('Ady', max_length=100)
    street = models.CharField('Köçe', max_length=100)
    house = models.CharField('Jaý', max_length=10)
    bloc = models.CharField('D/B', max_length=20)
    room = models.CharField('Otag', max_length=10)
    service = models.IntegerField('Hyzmat')
    old_number = models.CharField('Köne nomer', max_length=20)
    status = models.CharField('Status', max_length=100)
    etrap = models.ForeignKey(Etrap, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klientler'

    def __str__(self):
        return f'{self.name} {self.number}'