# Generated by Django 4.1.3 on 2022-12-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_dernierpublication_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entete',
            name='titre1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entete',
            name='titre2',
            field=models.TextField(),
        ),
    ]