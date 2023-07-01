# Generated by Django 4.2.2 on 2023-07-01 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_vendedor_foto_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='horario_abertura',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendedor',
            name='horario_fechamento',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
