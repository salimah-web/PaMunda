# Generated by Django 3.1.4 on 2020-12-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pamunda', '0005_auto_20201216_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]