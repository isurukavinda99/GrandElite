# Generated by Django 3.2.6 on 2021-08-19 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeePayments', '0004_auto_20210820_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='basicWage',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='empName',
        ),
    ]
