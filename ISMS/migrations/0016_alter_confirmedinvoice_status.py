# Generated by Django 3.2.6 on 2021-09-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISMS', '0015_auto_20210914_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmedinvoice',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('payment_done', 'Payment done')], default='pending', max_length=200, null=True),
        ),
    ]