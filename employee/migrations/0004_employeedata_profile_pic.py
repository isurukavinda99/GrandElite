# Generated by Django 3.2.6 on 2021-08-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210818_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedata',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]