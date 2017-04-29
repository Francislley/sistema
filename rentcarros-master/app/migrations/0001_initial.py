# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponibilidad', models.BooleanField(default=True, verbose_name='Disponibilidad')),
                ('modelo', models.CharField(max_length=150, verbose_name='Modelo')),
                ('combustible', models.CharField(choices=[('ds', 'Diesel'), ('gl', 'Gasolina'), ('hb', 'Hibrido'), ('gs', 'Gas'), ('el', 'Electrico')], default='ds', max_length=2)),
                ('anio', models.DateField(verbose_name='Año')),
                ('verificacion', models.BooleanField(verbose_name='Verificación')),
                ('personas', models.SmallIntegerField(verbose_name='Numero de Personas')),
                ('imagen_principal', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen Principal')),
                ('imagen_frontal', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen Frontal')),
                ('imagen_lateral_izq', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen Lateral Izquierda')),
                ('precio_por_dia', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'verbose_name_plural': 'Carros',
                'verbose_name': 'Carros',
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Equipamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cilindros', models.SmallIntegerField()),
                ('direccion', models.CharField(choices=[('Hidro', 'Hidraulica'), ('Asis', 'Asistida')], max_length=5, verbose_name='Dirección')),
                ('aire_acondicionado', models.BooleanField()),
                ('electrico', models.BooleanField()),
                ('transmicion', models.CharField(choices=[('Au', 'Automatico'), ('Ma', 'Manual'), ('Tri', 'Tipronic')], max_length=3, verbose_name='Transmición')),
                ('quemacocos', models.BooleanField()),
                ('asientos_de_piel', models.BooleanField()),
                ('gps', models.BooleanField()),
                ('color', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Equipamiento',
                'verbose_name': 'Equipamiento',
            },
        ),
        migrations.AddField(
            model_name='carro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Categorias'),
        ),
        migrations.AddField(
            model_name='carro',
            name='equipamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Equipamiento'),
        ),
    ]
