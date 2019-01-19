from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class BusinessUserViewSet(viewsets.ModelViewSet):
    queryset = BusinessUser.objects.all()
    serializer_class = BusinessUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
class CarFuelViewSet(viewsets.ModelViewSet):
    queryset = CarFuel.objects.all()
    serializer_class = CarFuelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class CarTransmissionViewSet(viewsets.ModelViewSet):
    queryset = CarTransmission.objects.all()
    serializer_class = CarTransmissionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class CarListViewSet(viewsets.ModelViewSet):
    queryset = CarList.objects.all()
    serializer_class = CarListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
class ServiceListViewSet(viewsets.ModelViewSet):
    queryset = ServiceList.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
class ServiceHistoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceHistory.objects.all()
    serializer_class = ServiceHistorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )