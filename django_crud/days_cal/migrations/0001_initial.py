# Generated by Django 4.1.5 on 2023-01-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField()),
                ('date2', models.DateField()),
                ('diff', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]
