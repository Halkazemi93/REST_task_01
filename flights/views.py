from .models import Flight, Booking
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import FlightSerializer, BookingSerializer
from datetime import datetime


class FlightListView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer 

class BookingListView(ListAPIView):
	queryset = Booking.objects.filter(date__gt=datetime.now())
	serializer_class = BookingSerializer
