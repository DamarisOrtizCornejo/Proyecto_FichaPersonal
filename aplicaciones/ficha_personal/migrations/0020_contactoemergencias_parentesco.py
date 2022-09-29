# Generated by Django 4.1.1 on 2022-09-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_personal', '0019_remove_contactoemergencias_parentesco'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactoemergencias',
            name='parentesco',
            field=models.CharField(blank=True, choices=[('M', 'Madre'), ('P', 'Padre'), ('H', 'Hermano(a)'), ('A', 'Abuelo(a)'), ('T', 'Tio(a)'), ('Pr', 'Primo(a)'), ('S', 'Sobrino(a)'), ('C', 'Cuñado(a)'), ('Pd', 'Padrastro'), ('Md', 'Madrastra'), ('Co', 'Conyuge'), ('Hi', 'Hijo(a)'), ('O', 'Otros')], default='M', max_length=2, null=True),
        ),
    ]
