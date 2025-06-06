# Generated by Django 5.1 on 2025-01-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imagerie", "0019_bdd_contact_identifiant_connect_modalite_connect_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bdd",
            name="projet",
        ),
        migrations.RemoveField(
            model_name="hard",
            name="modedegrade",
        ),
        migrations.RemoveField(
            model_name="hard",
            name="projet",
        ),
        migrations.RemoveField(
            model_name="resspartage",
            name="projet",
        ),
        migrations.RemoveField(
            model_name="soft",
            name="projet",
        ),
        migrations.AlterField(
            model_name="hard",
            name="stype",
            field=models.CharField(
                blank=True,
                choices=[("NA", "N/A"), ("VM", "PACS"), ("PHY", "PHYSIQUE")],
                default="NA",
                max_length=3,
                null=True,
            ),
        ),
    ]
