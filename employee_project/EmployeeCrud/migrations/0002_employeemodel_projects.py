# Generated by Django 4.1.5 on 2023-03-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeCrud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='Projects',
            field=models.JSONField(default=12),
            preserve_default=False,
        ),
    ]
