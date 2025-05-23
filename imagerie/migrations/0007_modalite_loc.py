# Generated by Django 5.1.3 on 2024-11-13 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imagerie", "0006_remove_modalite_nom_modalite_appareil_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="modalite",
            name="loc",
            field=models.ForeignKey(
                blank=True,
                help_text=" Localisation ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="loc_modalite",
                to="imagerie.localisation",
            ),
        ),
    ]
