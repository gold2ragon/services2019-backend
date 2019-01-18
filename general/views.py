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

from .models import Merchant
from .serializers import MerchantSerializer

class MerchantViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        # send_email_confirmation(user=self.request.user, modified=instance)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'merchants': reverse('merchant-list', request=request, format=format)
    })