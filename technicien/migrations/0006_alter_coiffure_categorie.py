# Generated by Django 4.1.3 on 2022-12-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicien', '0005_alter_agriculture_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coiffure',
            name='categorie',
            field=models.CharField(blank=True, default='coifure', max_length=150),
        ),
    ]