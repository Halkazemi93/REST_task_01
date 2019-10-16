from .models import Flight, Booking
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ["destination", "time", "price", "id"]

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ["flight", "date", "id"]


