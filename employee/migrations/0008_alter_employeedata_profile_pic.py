# Generated by Django 3.2.6 on 2021-08-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employeedata_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
