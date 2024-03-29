# Generated by Django 4.2.1 on 2023-05-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calculadora", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ciclo",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="ciclo",
            name="valor",
        ),
        migrations.RemoveField(
            model_name="periodo",
            name="nome",
        ),
        migrations.AddField(
            model_name="ciclo",
            name="numero",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="nota",
            name="materia",
            field=models.CharField(default="Valor Padrão", max_length=50),
        ),
        migrations.AddField(
            model_name="periodo",
            name="numero",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="nota",
            name="valor",
            field=models.FloatField(),
        ),
    ]
