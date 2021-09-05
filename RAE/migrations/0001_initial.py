# Generated by Django 3.2.6 on 2021-08-12 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=20)),
                ('event_type', models.CharField(choices=[('WEDDING', 'WEDDING'), ('BIRTHDAY', 'BIRTHDAY'), ('GETTOGETHER', 'GETTOGETHER'), ('SPECIAL', 'SPECIAL')], max_length=12)),
                ('package', models.CharField(choices=[('Package A', 'Package A'), ('Package B', 'Package B'), ('Package C', 'Package C')], max_length=10)),
                ('price', models.FloatField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(max_length=10)),
                ('customer_email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('AC', 'AC'), ('NON-AC', 'NON-AC'), ('DELUXE', 'DELUXE'), ('KING', 'KING')], max_length=7)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('RESERVED', 'RESERVED')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roombook_id', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(max_length=10)),
                ('customer_email', models.EmailField(max_length=254)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RAE.room')),
            ],
        ),
    ]