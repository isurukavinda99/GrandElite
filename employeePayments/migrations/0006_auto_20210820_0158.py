# Generated by Django 3.2.6 on 2021-08-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeePayments', '0005_auto_20210820_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='basicWage',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='payslip',
            name='empName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
