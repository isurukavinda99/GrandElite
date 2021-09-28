from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, FormView
from .models import Room, RoomBooking, EventBooking
from .forms import RoomForm, RoomBookingForm, EventBookingForm, RoomBookingUpdateForm

from django.template.loader import get_template
from xhtml2pdf import pisa

from CAS.decorators import *
from django.contrib.auth.decorators import login_required

# from .forms import AvailabilityForm
# from RAE.RBooking_functions.availability import check_availability

# Create your views here.

#create Room
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def createRoom(request):
    roomform = RoomForm()
    if request.method == 'POST':
        roomform = RoomForm(request.POST)
        if roomform.is_valid():
            roomform.save()
            messages.success(request, 'room added')
            return redirect('RAE:roomList')

    context = {'roomform': roomform}
    return render(request, 'RAE/createRoom.html', context)

#retrieve Room
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def roomList(request):
    room_data = Room.objects.all()
    context = {'room_data': room_data}
    return render(request, 'RAE/room_list.html', context)

#update Room
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def updateRoom(request, room_id):
    get_room_data = get_object_or_404(Room, room_id=room_id)
    roomform = RoomForm(instance=get_room_data)
    if request.method == 'POST':
        roomform = RoomForm(request.POST, instance=get_room_data)
        if roomform.is_valid():
            roomform.save()
            messages.success(request, 'Room Updated')
            return redirect('RAE:roomList')
    context = {'roomform': roomform}
    return render(request, 'RAE/updateRoom.html', context)

#search Room
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def searchRoom(request):
    if 'searchRoom' in request.GET:
        searchRoom = request.GET['searchRoom']
        room_data = Room.objects.filter(type__icontains=searchRoom)
    else:
        room_data = Room.objects.all()
    context = {'room_data': room_data}
    return render(request, 'RAE/room_list.html', context)


###########################################################

#create RoomBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def createRoomBooking(request):
    roombookingform = RoomBookingForm()
    if request.method == 'POST':
        roombookingform = RoomBookingForm(request.POST)
        if roombookingform.is_valid():
            roombookingform.save()
            messages.success(request, 'room booking added')
            return redirect('RAE:roomBookingList')

    context = {'roombookingform': roombookingform}
    return render(request, 'RAE/createRoomBooking.html', context)

#retrieve RoomBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def roomBookingList(request):
    roombooking_data = RoomBooking.objects.all()
    context = {'roombooking_data': roombooking_data}
    return render(request, 'RAE/roombooking_list.html', context)

#update RoomBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def updateRoomBooking(request, reserve_id):
    get_roombooking_data = get_object_or_404(RoomBooking, reserve_id=reserve_id)
    # roombookingform = RoomBookingForm(instance=get_roombooking_data)
    roombookingform = RoomBookingUpdateForm(instance=get_roombooking_data)
    if request.method == 'POST':
        roombookingform = RoomBookingUpdateForm(request.POST, instance=get_roombooking_data)
        if roombookingform.is_valid():
            roombookingform.save()
            messages.success(request, 'Room Reservation Updated')
            return redirect('RAE:roomBookingList')
    context = {'roombookingform': roombookingform}
    return render(request, 'RAE/updateRoomBooking.html', context)

#delete RoomBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def deleteRoomBooking(request, reserve_id):
    get_roombooking = get_object_or_404(RoomBooking, reserve_id=reserve_id)
    get_roombooking.delete()
    messages.success(request, 'Room Reservation Deleted')
    return redirect('RAE:roomBookingList')

#search roomBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def searchRoomBooking(request):
    if 'searchRoomBooking' in request.GET:
        searchRoomBooking = request.GET['searchRoomBooking']
        roombooking_data = RoomBooking.objects.filter(check_in__icontains=searchRoomBooking)
    else:
        roombooking_data = RoomBooking.objects.all()
    context = {'roombooking_data': roombooking_data}
    return render(request, 'RAE/roombooking_list.html', context)

#Generate Report
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def roomBookingPDF(request):
    roombooking_data = RoomBooking.objects.all()
    template_path = 'RAE/roomBookingReport.html'
    context = {'roombooking_data': roombooking_data}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="roomBookings_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

###########################################################

#create EventBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def createEventBooking(request):
    eventbookingform = EventBookingForm()
    if request.method == 'POST':
        eventbookingform = EventBookingForm(request.POST)
        if eventbookingform.is_valid():
            eventbookingform.save()
            messages.success(request, 'event added')
            return redirect('RAE:eventBookingList')

    context = {'eventbookingform': eventbookingform}
    return render(request, 'RAE/createEventBooking.html', context)

#retrieve EventBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def eventBookingList(request):
    eventbooking_data = EventBooking.objects.all()
    context = {'eventbooking_data': eventbooking_data}
    return render(request, 'RAE/eventbooking_list.html', context)

#update EventBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def updateEventBooking(request, event_id):
    get_eventbooking_data = get_object_or_404(EventBooking, event_id=event_id)
    eventbookingform = EventBookingForm(instance=get_eventbooking_data)
    if request.method == 'POST':
        eventbookingform = EventBookingForm(request.POST, instance=get_eventbooking_data)
        if eventbookingform.is_valid():
            eventbookingform.save()
            messages.success(request, 'Event Updated')
            return redirect('RAE:eventBookingList')
    context = {'eventbookingform': eventbookingform}
    return render(request, 'RAE/updateEventBooking.html', context)

#delete EventBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def deleteEventBooking(request, event_id):
    get_eventbooking = get_object_or_404(EventBooking, event_id=event_id)
    get_eventbooking.delete()
    messages.success(request, 'Event Deleted')
    return redirect('RAE:eventBookingList')

#search EventBooking
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def searchEventBooking(request):
    if 'searchEventBooking' in request.GET:
        searchEventBooking = request.GET['searchEventBooking']
        eventbooking_data = EventBooking.objects.filter(event_type__icontains=searchEventBooking)
    else:
        eventbooking_data = EventBooking.objects.all()
    context = {'eventbooking_data': eventbooking_data}
    return render(request, 'RAE/eventbooking_list.html', context)

#Generate Report
@login_required(login_url='login')
@allowed_users(allowed_roles=['RAE'])
def eventBookingPDF(request):
    eventbooking_data = EventBooking.objects.all()
    template_path = 'RAE/eventBookingReport.html'
    context = {'eventbooking_data': eventbooking_data}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="eventBookings_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# class RoomsList(ListView):
#         model = Room
#
# class RoomBookingList(ListView):
#         model = RoomBooking
#
# class EventBookingList(ListView):
#         model = EventBooking
#
# class BookingView(FormView):
#     form_class = AvailabilityForm
#     template_name = 'RAE/availability_form.html'
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         room_list = Room.objects.filter(type=data['room_type'])
#         available_rooms = []
#         for room in room_list:
#             if check_availability(room, data['check_in'], data['check_out']):
#                 available_rooms.append(room)
#
#         if len(available_rooms) > 0:
#             room = available_rooms[0]
#             roombooking= RoomBooking.objects.create(
#                 room_Id=room,
#                 check_in=data['check_in'],
#                 check_out=data['check_out']
#             )
#             roombooking.save()
#             return HttpResponse(roombooking)
#         else:
#             return HttpResponse('All of this type of rooms are booked!! Try another one')
#

