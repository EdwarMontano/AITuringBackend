# Generated by Django 4.0 on 2022-03-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
