# Generated by Django 4.1.5 on 2023-01-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('dept', models.CharField(max_length=25)),
            ],
        ),
    ]
