# Generated by Django 3.1 on 2022-10-27 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20221026_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atraso',
            name='Nombre_Responsable',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='problema',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='Funcionario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Diseñador de Flujo'),
        ),
    ]