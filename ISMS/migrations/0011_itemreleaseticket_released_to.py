# Generated by Django 3.2.6 on 2021-09-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISMS', '0010_itemreleaseticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemreleaseticket',
            name='released_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
