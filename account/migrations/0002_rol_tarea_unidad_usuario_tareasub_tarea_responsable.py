# Generated by Django 4.1 on 2022-10-10 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_R', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Tarea', models.CharField(max_length=50)),
                ('Fecha_desde', models.DateField()),
                ('Fecha_hasta', models.DateField()),
                ('Descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_U', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Jerarquia', models.CharField(max_length=50)),
                ('Rol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.rol')),
                ('Unidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='TareaSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_TareaS', models.CharField(max_length=50)),
                ('Fecha_desdeS', models.DateField()),
                ('Fecha_hastaS', models.DateField()),
                ('DescripcionS', models.TextField()),
                ('ResponsableS', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.usuario')),
                ('TareaMadreS', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.tarea')),
            ],
        ),
        migrations.AddField(
            model_name='tarea',
            name='Responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.usuario'),
        ),
    ]
