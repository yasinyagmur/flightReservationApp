from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FlightSerializer,ReservationSerializer
from .models import Flight,Reservation
from rest_framework.permissions import IsAdminUser
from .permissions import IsStafforReadOnly
# Create your views here.

class FligtView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user = self.request.user)