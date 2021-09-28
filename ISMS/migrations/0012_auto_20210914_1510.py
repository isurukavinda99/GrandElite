# Generated by Django 3.1.6 on 2021-09-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISMS', '0011_itemreleaseticket_released_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmail',
            name='status',
            field=models.CharField(blank=True, choices=[('requested', 'Requested'), ('suppler_confirmed', 'Suppler confirmed'), ('payment_done', 'Payment done')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itemreleaseticket',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='itemreleaseticket',
            name='released_to',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sendmail',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
