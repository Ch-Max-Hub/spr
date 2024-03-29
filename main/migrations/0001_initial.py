# Generated by Django 5.0.2 on 2024-03-03 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etrap_code', models.IntegerField(verbose_name='Etrap kod')),
                ('etrap_name', models.CharField(max_length=100, verbose_name='Ady')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.etrap', verbose_name='Degişli etraby')),
            ],
            options={
                'verbose_name': 'Etrap',
                'verbose_name_plural': 'Etraplar',
                'unique_together': {('etrap_name', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('etrap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.etrap')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Nomer')),
                ('name', models.CharField(max_length=100, verbose_name='Ady')),
                ('street', models.CharField(max_length=100, verbose_name='Köçe')),
                ('house', models.CharField(max_length=10, verbose_name='Jaý')),
                ('bloc', models.CharField(blank=True, max_length=20, null=True, verbose_name='D/B')),
                ('room', models.CharField(blank=True, max_length=10, null=True, verbose_name='Otag')),
                ('service', models.IntegerField(blank=True, null=True, verbose_name='Hyzmat')),
                ('old_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Köne nomer')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Status')),
                ('etrap', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.etrap')),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klientler',
            },
        ),
    ]
