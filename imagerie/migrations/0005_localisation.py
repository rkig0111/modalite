# Generated by Django 5.1.3 on 2024-11-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imagerie", "0004_alter_pacs_net_alter_printer_net_alter_store_net_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Localisation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=30, null=True)),
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                "db_table": "Localisation",
                "managed": True,
            },
        ),
    ]
