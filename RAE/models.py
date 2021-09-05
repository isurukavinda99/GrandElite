from django.db import models
from django.conf import settings

# Create your models here.
from django.db.models import ForeignKey


class Room(models.Model):
    ROOM_TYPES = (
        ('', 'SELECT'),
        ('AC', 'AC'),
        ('NON-AC', 'NON-AC'),
        ('DELUXE', 'DELUXE'),
        ('KING', 'KING'),
    )
    ROOM_STATUS = (
        ('AVAILABLE', 'AVAILABLE'),
        ('RESERVED', 'RESERVED'),
    )

    room_id = models.CharField(max_length=20)
    type = models.CharField(max_length=7, choices=ROOM_TYPES)
    price = models.FloatField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=ROOM_STATUS, default=None)

    def __str__(self):
        return f'{self.room_id}'


class RoomBooking(models.Model):
        reserve_id = models.CharField(max_length=20)
        room_Id = models.ForeignKey(Room, on_delete=models.CASCADE)
        customer_name = models.CharField(max_length=50)
        customer_phone = models.CharField(max_length=10)
        customer_email = models.EmailField()
        check_in = models.DateTimeField()
        check_out = models.DateTimeField()

        def __str__(self):
            return f'{self.reserve_id} {self.room_Id} has booked by {self.customer_name} {self.customer_phone} {self.customer_email} from {self.check_in} to {self.check_out} '


class EventBooking(models.Model):
    EVENT_TYPES = (
        ('', 'SELECT'),
        ('WEDDING', 'WEDDING'),
        ('BIRTHDAY', 'BIRTHDAY'),
        ('GETTOGETHER', 'GETTOGETHER'),
        ('SPECIAL', 'SPECIAL'),
    )

    EVENT_PACKAGES = (
        ('Package A', 'Package A'),
        ('Package B', 'Package B'),
        ('Package C', 'Package C'),
    )

    event_id = models.CharField(max_length=20)
    event_type = models.CharField(max_length=12, choices=EVENT_TYPES)
    package = models.CharField(max_length=10, choices=EVENT_PACKAGES, default=None)
    price = models.FloatField()
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=10)
    customer_email = models.EmailField()
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self):
        return f'{self.event_id} {self.event_type} {self.package} at {self.price} has booked by {self.customer_name} {self.customer_phone} {self.customer_email} on {self.date} from {self.time_in} to {self.time_out} '



