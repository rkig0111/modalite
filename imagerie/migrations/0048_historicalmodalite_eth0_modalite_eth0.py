# Generated by Django 5.2.3 on 2025-06-27 10:21

import macaddress.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagerie', '0047_remove_historicalmodalite_ping'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmodalite',
            name='eth0',
            field=macaddress.fields.MACAddressField(blank=True, integer=False, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='modalite',
            name='eth0',
            field=macaddress.fields.MACAddressField(blank=True, integer=False, max_length=17, null=True),
        ),
    ]
