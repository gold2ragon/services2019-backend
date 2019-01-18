from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'email', 'tel', 'address')

class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Merchant
        fields = ( 'url', 'user', 'company_name', 'autoservice_name', 'reg', 'vat', 'iban', 'description', 'photo_url')
    
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        merchant, created = Merchant.objects.update_or_create(user=user,
                            company_name=validated_data.pop('company_name'), 
                            autoservice_name=validated_data.pop('autoservice_name'), 
                            reg=validated_data.pop('reg'), 
                            vat=validated_data.pop('vat'), 
                            iban=validated_data.pop('iban'),
                            description=validated_data.pop('description'), 
                            photo_url=validated_data.pop('photo_url'),  )
        return merchant