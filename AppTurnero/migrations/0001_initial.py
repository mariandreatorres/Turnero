# Generated by Django 4.2.5 on 2023-09-27 01:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosProfesionales',
            fields=[
                ('id_profesional', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=60)),
                ('apellido', models.CharField(default='', max_length=60)),
                ('mail', models.CharField(default='', max_length=60)),
                ('cuit', models.CharField(default='', max_length=10)),
                ('razon_social', models.CharField(default='', max_length=60)),
                ('especialidad', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=60)),
                ('apellido', models.CharField(default='', max_length=60)),
                ('obra_social', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Meses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(default='202301', max_length=10)),
                ('fecha', models.DateField(default=datetime.datetime.today)),
                ('hora', models.DateTimeField(default=datetime.datetime.now)),
                ('id_profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTurnero.datosprofesionales')),
            ],
        ),
        migrations.CreateModel(
            name='HorariosProfesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(default='', max_length=10)),
                ('hora_inicio', models.CharField(default='', max_length=10)),
                ('hora_fin', models.CharField(default='', max_length=10)),
                ('id_profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTurnero.datosprofesionales')),
            ],
        ),
    ]
