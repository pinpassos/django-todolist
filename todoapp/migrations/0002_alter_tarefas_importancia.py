# Generated by Django 3.2.6 on 2021-08-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefas',
            name='importancia',
            field=models.IntegerField(max_length=2),
        ),
    ]
