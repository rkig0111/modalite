# Generated by Django 4.0 on 2024-11-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagerie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalite',
            name='printer',
            field=models.ManyToManyField(blank=True, help_text=" différents PRINT où l'on peut imprimer les examens", related_name='printer_modalite', to='imagerie.Printer'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='store',
            field=models.ManyToManyField(blank=True, help_text=" différents STORE où l'on peut pousser les examens", related_name='store_modalite', to='imagerie.Store'),
        ),
    ]
