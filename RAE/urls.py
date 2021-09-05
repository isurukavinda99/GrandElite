
from django.contrib import admin
from django.urls import path, include
from . views import createRoom, roomList, updateRoom, searchRoom, createRoomBooking, roomBookingList, updateRoomBooking, deleteRoomBooking, searchRoomBooking, roomBookingPDF, createEventBooking, eventBookingList, updateEventBooking,  deleteEventBooking, searchEventBooking, eventBookingPDF
# from . views import RoomsList, RoomBookingList, EventBookingList, BookingView


app_name = 'RAE'

urlpatterns = [
      #room
      path('addroom/', createRoom, name='createRoom'),
      path('room_list/', roomList, name='roomList'),
      path('room_list/<room_id>/', updateRoom, name='updateRoom'),
      path('search_room/', searchRoom, name='searchRoom'),


      #roombooking
      path('addroombooking/', createRoomBooking, name='createRoomBooking'),
      path('roombooking_list/', roomBookingList, name='roomBookingList'),
      path('roombooking_list/<reserve_id>/', updateRoomBooking, name='updateRoomBooking'),
      path('roombooking_list/delete/<reserve_id>/', deleteRoomBooking, name='deleteRoomBooking'),
      path('search_roombooking/', searchRoomBooking, name='searchRoomBooking'),
      path('roombooking_pdf/', roomBookingPDF, name='roomBookingPDF'),


      #eventbooking
      path('addevent/', createEventBooking, name='createEventBooking'),
      path('eventbooking_list/', eventBookingList, name='eventBookingList'),
      path('eventbooking_list/<event_id>/', updateEventBooking, name='updateEventBooking'),
      path('eventbooking_list/delete/<event_id>/', deleteEventBooking, name='deleteEventBooking'),
      path('search_eventbooking/', searchEventBooking, name='searchEventBooking'),
      path('eventbooking_pdf/', eventBookingPDF, name='eventBookingPDF'),

      # path('room_list/', RoomsList.as_view(), name='RoomList'),
      # path('roombooking_list/', RoomBookingList.as_view(), name='RoomBookingList'),
      # path('eventbooking_list/', EventBookingList.as_view(), name='EventBookingList'),
      # path('roombook/', BookingView.as_view(), name='booking_view'),
]
