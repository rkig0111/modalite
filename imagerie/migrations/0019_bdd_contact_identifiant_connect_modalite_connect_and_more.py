# Generated by Django 5.1 on 2025-01-03 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imagerie", "0018_alter_modalite_serveur"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bdd",
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
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                ("unc", models.CharField(blank=True, max_length=200, null=True)),
                ("host", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "port",
                    models.IntegerField(blank=True, help_text=" Port BDD ", null=True),
                ),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "Bdd",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("societe", models.CharField(blank=True, max_length=30, null=True)),
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                ("prenom", models.CharField(blank=True, max_length=30, null=True)),
                ("mail", models.EmailField(blank=True, max_length=50, null=True)),
                ("telmobile", models.CharField(blank=True, max_length=30, null=True)),
                ("telfixe", models.CharField(blank=True, max_length=30, null=True)),
                ("dect", models.CharField(blank=True, max_length=30, null=True)),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "Contact",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Identifiant",
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
                ("login", models.CharField(blank=True, max_length=30, null=True)),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "Identifiant",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Connect",
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
                (
                    "bdd",
                    models.ForeignKey(
                        blank=True,
                        help_text=" connexion à BDD ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="connect_bdd",
                        to="imagerie.bdd",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="modalite",
            name="connect",
            field=models.OneToOneField(
                blank=True,
                help_text=" connnectivité de la machine ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modalite_connect",
                to="imagerie.connect",
            ),
        ),
        migrations.CreateModel(
            name="Hard",
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
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "stype",
                    models.CharField(
                        blank=True,
                        default="VM",
                        help_text=" VM / Physique ",
                        max_length=30,
                        null=True,
                    ),
                ),
                ("ram", models.CharField(blank=True, max_length=10, null=True)),
                ("core", models.IntegerField(blank=True, null=True)),
                ("ddsystem", models.CharField(blank=True, max_length=10, null=True)),
                ("dddata", models.CharField(blank=True, max_length=10, null=True)),
                ("editeur", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "modedegrade",
                    models.TextField(
                        blank=True,
                        help_text=" mode #dégradé à mettre en place.. ",
                        null=True,
                    ),
                ),
                (
                    "doc",
                    models.FileField(blank=True, null=True, upload_to="documentations"),
                ),
                ("divers", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "bdd",
                    models.ForeignKey(
                        blank=True,
                        help_text=" Base de données ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ordi_bdd",
                        to="imagerie.bdd",
                    ),
                ),
            ],
            options={
                "db_table": "Hard",
                "ordering": ["nom"],
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="modalite",
            name="hard",
            field=models.OneToOneField(
                blank=True,
                help_text=" configuration matérielle de la machine ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modalite_hard",
                to="imagerie.hard",
            ),
        ),
        migrations.AddField(
            model_name="bdd",
            name="identifiant",
            field=models.ManyToManyField(
                help_text=" Identifiant # ", to="imagerie.identifiant"
            ),
        ),
        migrations.CreateModel(
            name="Projet",
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
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                ("demande", models.CharField(blank=True, max_length=50, null=True)),
                ("editeur", models.CharField(blank=True, max_length=50, null=True)),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "doc",
                    models.FileField(blank=True, null=True, upload_to="documentations"),
                ),
                (
                    "datecreat",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "datemodif",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "datefin",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de finalisation"
                    ),
                ),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        help_text=" Contact ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="projet_contact",
                        to="imagerie.contact",
                    ),
                ),
                (
                    "hard",
                    models.ManyToManyField(
                        blank=True,
                        help_text=" matériels achetés, fournis... ",
                        related_name="projet_hard",
                        to="imagerie.hard",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        blank=True,
                        help_text=" Service ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="projet_service",
                        to="imagerie.service",
                    ),
                ),
            ],
            options={
                "db_table": "Projet",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="hard",
            name="projet",
            field=models.ForeignKey(
                blank=True,
                help_text=" Projet ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ordi_projet",
                to="imagerie.projet",
            ),
        ),
        migrations.AddField(
            model_name="bdd",
            name="projet",
            field=models.ForeignKey(
                blank=True,
                help_text=" Projet ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bdd_projet",
                to="imagerie.projet",
            ),
        ),
        migrations.CreateModel(
            name="Ras",
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
                ("denom", models.CharField(blank=True, max_length=30, null=True)),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        help_text=" Contact ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ras_contact",
                        to="imagerie.contact",
                    ),
                ),
            ],
            options={
                "db_table": "Ras",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="connect",
            name="ras",
            field=models.ForeignKey(
                blank=True,
                help_text=" compte ras_xxx ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="connect_ras",
                to="imagerie.ras",
            ),
        ),
        migrations.CreateModel(
            name="Resspartage",
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
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                ("chemin", models.CharField(blank=True, max_length=255, null=True)),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "identifiant",
                    models.ManyToManyField(
                        help_text=" Identifiant # ", to="imagerie.identifiant"
                    ),
                ),
                (
                    "projet",
                    models.ForeignKey(
                        blank=True,
                        help_text=" Projet ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="resspartage_projet",
                        to="imagerie.projet",
                    ),
                ),
            ],
            options={
                "db_table": "Resspartage",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="hard",
            name="resspartage",
            field=models.ForeignKey(
                blank=True,
                help_text=" #Ressource partagée ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ordi_resspartage",
                to="imagerie.resspartage",
            ),
        ),
        migrations.AddField(
            model_name="connect",
            name="resspartage",
            field=models.ForeignKey(
                blank=True,
                help_text=" ressource partagée ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="connect_resspartage",
                to="imagerie.resspartage",
            ),
        ),
        migrations.CreateModel(
            name="Soft",
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
                ("os", models.CharField(blank=True, max_length=30, null=True)),
                ("nom", models.CharField(blank=True, max_length=30, null=True)),
                ("version", models.CharField(blank=True, max_length=30, null=True)),
                ("referent", models.CharField(blank=True, max_length=30, null=True)),
                ("divers", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "projet",
                    models.ForeignKey(
                        blank=True,
                        help_text=" Projet ",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="soft_projet",
                        to="imagerie.projet",
                    ),
                ),
            ],
            options={
                "db_table": "Logiciel",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="projet",
            name="softs",
            field=models.ManyToManyField(
                blank=True,
                help_text=" Logiciels achetés, fournis...",
                related_name="projet_soft",
                to="imagerie.soft",
            ),
        ),
        migrations.AddField(
            model_name="modalite",
            name="soft",
            field=models.OneToOneField(
                blank=True,
                help_text=" configuration logicielle de la machine ",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modalite_soft",
                to="imagerie.soft",
            ),
        ),
    ]
