# Generated by Django 3.2.6 on 2021-08-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeePayments', '0009_auto_20210820_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='basicWage',
            field=models.FloatField(null=True),
        ),
    ]
