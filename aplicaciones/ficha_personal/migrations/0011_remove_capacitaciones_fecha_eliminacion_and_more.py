# Generated by Django 4.1.1 on 2022-09-19 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_personal', '0010_sueldo_estado_alter_infoacademica_institucion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitaciones',
            name='fecha_eliminacion',
        ),
        migrations.RemoveField(
            model_name='capacitaciones',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='capacitaciones',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='capacitaciones',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='contactoemergencias',
            name='fecha_eliminacion',
        ),
        migrations.RemoveField(
            model_name='contactoemergencias',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='contactoemergencias',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='contactoemergencias',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='infoacademica',
            name='fecha_eliminacion',
        ),
        migrations.RemoveField(
            model_name='infoacademica',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='infoacademica',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='infoacademica',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='sueldo',
            name='fecha_eliminacion',
        ),
        migrations.RemoveField(
            model_name='sueldo',
            name='fecha_modificacion',
        ),
        migrations.RemoveField(
            model_name='sueldo',
            name='fecha_registro',
        ),
        migrations.RemoveField(
            model_name='sueldo',
            name='usuario',
        ),
    ]
