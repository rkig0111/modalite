# Generated by Django 5.1.5 on 2025-06-16 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagerie', '0041_historicalmodalite_n_invent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmodalite',
            name='Connection',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.connection'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='aet',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='appareil',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.appareil'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='appareiltype',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.appareiltype'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='hard',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.hard'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='loc',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.localisation'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='pacs',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.modalite'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='ping',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='reforme',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='service',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.service'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='vlan',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.vlan'),
        ),
        migrations.AlterField(
            model_name='historicalmodalite',
            name='worklist',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imagerie.modalite'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='Connection',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_Connection', to='imagerie.connection'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='aet',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='appareil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_appareil', to='imagerie.appareil'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='appareiltype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_appareiltype', to='imagerie.appareiltype'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='hard',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_hard', to='imagerie.hard'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='loc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_loc', to='imagerie.localisation'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='pacs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_pacs', to='imagerie.modalite'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='ping',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='printers',
            field=models.ManyToManyField(blank=True, related_name='modalite_printers', to='imagerie.modalite'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='reforme',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_service', to='imagerie.service'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='stores',
            field=models.ManyToManyField(blank=True, related_name='modalite_stores', to='imagerie.modalite'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='vlan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='net_vlan', to='imagerie.vlan'),
        ),
        migrations.AlterField(
            model_name='modalite',
            name='worklist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='modalite_worklist', to='imagerie.modalite'),
        ),
    ]
