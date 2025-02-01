from rest_framework import viewsets
from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer
from listings.tasks import send_booking_confirmation_email

class PropertyViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing CRUD operations on Property model.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for performing CRUD operations on Booking model.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        send_booking_confirmation_email.delay(booking.id, booking.user.email)
