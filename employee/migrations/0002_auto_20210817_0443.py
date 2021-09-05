# Generated by Django 3.2.6 on 2021-08-16 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedata',
            name='basicSalary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.salarygroup'),
        ),
        migrations.AddField(
            model_name='employeedata',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='employee.jobroles'),
        ),
        migrations.AlterField(
            model_name='jobroles',
            name='jobRole',
            field=models.CharField(max_length=20),
        ),
    ]
