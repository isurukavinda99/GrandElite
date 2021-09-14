# Generated by Django 3.2.6 on 2021-09-09 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ISMS', '0009_alter_sendmail_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemReleaseTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('released_quantity', models.IntegerField()),
                ('current_quantity', models.IntegerField()),
                ('released_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='release_item', to='ISMS.item')),
            ],
        ),
    ]