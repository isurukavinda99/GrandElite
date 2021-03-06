# Generated by Django 3.2.6 on 2021-08-18 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210817_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='basicSalary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.salarygroup'),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.jobroles'),
        ),
    ]
