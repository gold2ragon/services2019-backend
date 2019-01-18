from rest_framework import serializers
from .models import Merchant
from django.contrib.auth.models import User

class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    merchants = serializers.HyperlinkedRelatedField(many=True, view_name='merchant-detail', read_only=True)

    class Meta:
        model = Merchant
        fields = '__all__'