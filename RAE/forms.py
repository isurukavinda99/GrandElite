from django import forms
from .models import Room, RoomBooking, EventBooking

# Room
class RoomForm(forms.ModelForm):
    room_id = forms.CharField(label='Room ID', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room ID'}),
    required=True, error_messages={'required': 'Must Enter a correct Room ID'})
    price = forms.FloatField(label='Price (Rs.)', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Price'}),
    required=True, error_messages={'required': 'Must Enter a valid price in Rupees'})
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Room Description'}),
    required=True, error_messages={'required': 'Must Enter a room description'})

    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'type': {'required': 'Must Select a room type'},
            'status': {'required': 'Must Select a room status'}
        }

# ###############################################################

# RoomBooking
class RoomBookingForm(forms.ModelForm):
    reserve_id = forms.CharField(label='Reservation ID', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Room Reservation ID'}),
    required = True, error_messages={'required': 'Must Enter a correct Room Reservation ID'})
    # room_Id = forms.CharField(label='Room ID', chooses=Room.objects.all(),
    # required = True, error_messages={'required': 'Must Enter a correct Room ID'})
    customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Name'}),
    required=True, error_messages={'required': 'Must Enter a customer name'})
    customer_phone = forms.CharField(label='Customer Phone', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Phone Number'}),
    required=True, error_messages={'required': 'Must Enter a customer phone number'})
    customer_email = forms.EmailField(label='Customer Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Email'}),
    required=True, error_messages={'required': 'Must Enter a customer email'})
    # check_in = forms.DateTimeField(label='Check-in', required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
    # error_messages={'required': 'Must Select check-in date and time'})
    # check_out = forms.DateTimeField(label='Check-out', required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"], widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
    # error_messages={'required': 'Must Select check-out date and time'})

    class Meta:
        model = RoomBooking
        fields = '__all__'
        widgets = {
            'check_in': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Check-in'}),
            'check_out': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Check-out'}),
        }
        error_messages = {
            # 'reserve_id': {'required': 'Must Enter a correct Room Reservation ID'},
            'room_Id': {'required': 'Must Enter a correct Room ID'},
            # 'customer_name': {'required': 'Must Enter a customer name'},
            # 'customer_phone': {'required': 'Must Enter a customer phone number'},
            # 'customer_email': {'required': 'Must Enter a customer email'},
            'check_in': {'required': 'Must Enter check-in date and time'},
            'check_out': {'required': 'Must Enter check-out date and time'},
        }


# ###############################################################

# EventBooking
class EventBookingForm(forms.ModelForm):
    event_id = forms.CharField(label='Event ID', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Event ID'}),
    required=True, error_messages={'required': 'Must Enter a correct Event ID'})
    price = forms.FloatField(label='Price (Rs.)', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Price'}),
    required=True, error_messages={'required': 'Must Enter a valid price in Rupees'})
    customer_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Name'}),
    required=True, error_messages={'required': 'Must Enter a customer name'})
    customer_phone = forms.CharField(label='Customer Phone', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Phone Number'}),
    required=True, error_messages={'required': 'Must Enter a customer phone number'})
    customer_email = forms.EmailField(label='Customer Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Customer Email'}),
    required=True, error_messages={'required': 'Must Enter a customer email'})
    date = forms.DateField(label='Event Date', input_formats=["%Y-%m-%d", "%Y-%m-%d"], widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    required=True, error_messages={'required': 'Must Select an event date'})
    time_in = forms.TimeField(label='Time-in', input_formats=["%H:%M", "%H:%M"], widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
    required=False, error_messages={'required': 'Must Select time-in'})
    time_out = forms.TimeField(label='Time-out', input_formats=["%H:%M", "%H:%M"], widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
    required=False, error_messages={'required': 'Must Select time-out'})


    class Meta:
        model = EventBooking
        fields = '__all__'
        widgets = {
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'package': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'event_type': {'required': 'Must Select an event type'},
            'package': {'required': 'Must Select an event package'}
        }

# ###############################################################


# class AvailabilityForm(forms.Form):
#     ROOM_TYPES = (
#         ('YAC', 'AC'),
#         ('NAC', 'NON-AC'),
#         ('DEL', 'DELUXE'),
#         ('KIN', 'KING'),
#     )
#     room_type = forms.ChoiceField(choices=ROOM_TYPES, required=True)
#     check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"],
#     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M%Z"],
#     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
