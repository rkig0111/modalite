# Generated by Django 5.1.5 on 2025-01-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagerie', '0033_modalite_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='nom',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='nom',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='societe',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='identifiant',
            name='login',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='projet',
            name='nom',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='ras',
            name='denom',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='resspartage',
            name='nom',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
