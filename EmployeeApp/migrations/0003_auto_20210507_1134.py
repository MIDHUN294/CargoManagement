# Generated by Django 3.1.6 on 2021-05-07 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_auto_20210507_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetailstb',
            old_name='Customer',
            new_name='CustomerName',
        ),
    ]
