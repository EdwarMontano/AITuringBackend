# Generated by Django 4.0 on 2022-03-05 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=200, verbose_name='Categoría')),
                ('category_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('category_modifed', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name_category'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('ciudad_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('ciudad_modifed', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pais', models.CharField(max_length=100, verbose_name='País')),
                ('pais_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('pais_modifed', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
                'ordering': ['name_pais'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cliente', models.CharField(max_length=200, verbose_name='Nombre')),
                ('is_admin', models.BooleanField(default=False)),
                ('user_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('user_modifed', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.city')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.pais')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['name_cliente'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.pais'),
        ),
    ]