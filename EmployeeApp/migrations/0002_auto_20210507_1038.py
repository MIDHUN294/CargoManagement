# Generated by Django 3.1.6 on 2021-05-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetailstb',
            name='Address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='Amount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='Customer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='DeliveryAcceptDate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='Destination',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='District',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='EmailID',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='MobileNumber',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='PackegeType',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='Status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customerdetailstb',
            name='Weight',
            field=models.CharField(default='', max_length=100),
        ),
    ]
