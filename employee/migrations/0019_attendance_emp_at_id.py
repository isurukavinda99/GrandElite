# Generated by Django 3.2.6 on 2021-09-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_auto_20210916_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='emp_at_id',
            field=models.IntegerField(null=True),
        ),
    ]
