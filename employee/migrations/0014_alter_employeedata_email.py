# Generated by Django 3.2.6 on 2021-08-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_auto_20210821_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]
