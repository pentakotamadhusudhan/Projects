# Generated by Django 2.2.27 on 2022-04-12 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country_currency', '0004_auto_20220411_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency_symbol',
            old_name='country_currency',
            new_name='country',
        ),
    ]
