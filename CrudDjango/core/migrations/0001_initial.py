# Generated by Django 4.0.2 on 2022-06-08 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='marca vehiculo')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='modelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
