from django.contrib.auth.models import User
from django.db import models


class Etrap(models.Model):
    code = models.IntegerField('Etrap kod')
    name = models.CharField('Ady', max_length=100)
    parent = models.ForeignKey('self', verbose_name='Degişli etraby', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        unique_together = ['name', 'parent']
        verbose_name = 'Etrap'
        verbose_name_plural = 'Etraplar'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.parent:
            self.code = self.parent.code
        super().save(*args, **kwargs)


class UserEtrap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    etrap = models.ForeignKey(Etrap, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Ulanyjynyň degişli etraby'
        verbose_name_plural = 'Ulanyjynyň degişli etraby'

    def __str__(self):
        return f'{self.user} {self.etrap}'


class Client(models.Model):
    number = models.CharField('Nomer', max_length=20)
    name = models.CharField('Ady', max_length=100)
    street = models.CharField('Köçe', max_length=100, blank=True, null=True)
    house = models.CharField('Jaý', max_length=10, blank=True, null=True)
    bloc = models.CharField('D/B', max_length=20, blank=True, null=True)
    room = models.CharField('Otag', max_length=10, blank=True, null=True)
    service = models.IntegerField('Hyzmat', blank=True, null=True)
    old_number = models.CharField('Köne nomer', max_length=20, blank=True, null=True)
    status = models.CharField('Status', max_length=100, blank=True, null=True)
    etrap = models.ForeignKey(Etrap, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klientler'

    def __str__(self):
        return f'{self.name} {self.number}'