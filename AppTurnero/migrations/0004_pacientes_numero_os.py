# Generated by Django 4.2.5 on 2023-10-03 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnero', '0003_pacientes_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='numero_os',
            field=models.IntegerField(default=0),
        ),
    ]
