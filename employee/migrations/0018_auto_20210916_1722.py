# Generated by Django 3.2.6 on 2021-09-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20210916_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='inTime',
            field=models.TimeField(null=True),
        ),
    ]
