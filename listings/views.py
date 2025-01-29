from rest_framework import viewsets
from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer

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
