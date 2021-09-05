# Generated by Django 3.2.6 on 2021-08-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeePayments', '0007_auto_20210820_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='empAllow',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='empDed',
        ),
        migrations.AddField(
            model_name='payslip',
            name='month',
            field=models.CharField(max_length=15, null=True),
        ),
    ]