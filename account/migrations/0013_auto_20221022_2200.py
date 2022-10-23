# Generated by Django 3.1 on 2022-10-23 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20221021_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.tarea')),
            ],
        ),
        migrations.RemoveField(
            model_name='tareasub',
            name='Responsable',
        ),
        migrations.AddField(
            model_name='tareasub',
            name='ResponsableS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='account.usuario'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TareaAce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Ta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.tarea2')),
                ('TareaAce', models.ManyToManyField(blank=True, null=True, to='account.Tarea')),
            ],
        ),
    ]
