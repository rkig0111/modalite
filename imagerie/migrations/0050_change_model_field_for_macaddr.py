from __future__ import unicode_literals

from django.apps import apps
from django.db import migrations, models
from django.db.models import F


def copy_field(apps, schema):
    MyModel = apps.get_model('imagerie', 'Modalite')
    MyModel.objects.all().update(macaddr2=F('macaddr'))

class Migration(migrations.Migration):
    dependencies = [
        ('imagerie', '0049_rename_eth0_historicalmodalite_macaddr2_and_more'),
    ]

    operations = [
        migrations.RunPython(code=copy_field),
    ]