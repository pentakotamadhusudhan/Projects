# Generated by Django 4.1.5 on 2023-01-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decimalmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField()),
                ('digits', models.IntegerField()),
                ('decimal_value', models.CharField(max_length=100)),
            ],
        ),
    ]
