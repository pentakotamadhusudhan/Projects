# Generated by Django 4.0.3 on 2022-04-06 10:48

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency_symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_currency', django_countries.fields.CountryField(max_length=2)),
                ('currency', models.CharField(max_length=50)),
                ('currency_symbol', models.TextField(max_length=50)),
            ],
        ),
    ]
