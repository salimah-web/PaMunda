# Generated by Django 3.1.4 on 2020-12-15 23:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pamunda', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prod',
            new_name='Product',
        ),
    ]
