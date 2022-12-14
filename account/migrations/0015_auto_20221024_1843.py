# Generated by Django 3.1 on 2022-10-24 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20221024_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareasub',
            name='ResponsableS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoProblema', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Asignacion Tarea'), (2, 'Fechas'), (3, 'Reclamo'), (4, 'Sugerencia Tarea'), (5, 'Otro')], default=0, null=True)),
                ('Estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Revision'), (2, 'Respondido'), (3, 'Cerrado')], default=1, null=True)),
                ('Nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atraso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Revision'), (2, 'Respondido')], default=1, null=True)),
                ('Nombre_Responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Nombre_Tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.tarea')),
            ],
        ),
    ]
