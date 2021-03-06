# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 15:24
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('num_tel', models.IntegerField(verbose_name='numero telefonico')),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('r_con', models.BooleanField(default=False)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Carro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reservaciones',
                'verbose_name': 'Reservaciones',
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_tarjeta', models.IntegerField(verbose_name='Numero de tarjeta')),
                ('codigo_cvc', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('fecha_expiracion', models.DateField()),
                ('terminos_condiciones', models.BooleanField(verbose_name='Acepto politicas terminos y condiciones.')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
