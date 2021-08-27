# Generated by Django 3.2.6 on 2021-08-24 20:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_alter_tarefas_importancia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='importancia',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2)]),
        ),
    ]