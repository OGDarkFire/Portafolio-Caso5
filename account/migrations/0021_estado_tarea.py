# Generated by Django 3.1 on 2022-11-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20221119_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completado', models.BooleanField(default=False)),
                ('Nombre_Tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.tarea')),
            ],
        ),
    ]