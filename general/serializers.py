from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'name', 'surname', 'email', 'tel', 'address')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

class MerchantSerializer(serializers.ModelSerializer):
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
                            description=validated_data.pop('description'), )
        try:
            merchant.photo_url=validated_data.pop('photo_url')
            merchant.save()
        except:
            pass    
        return merchant
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        username = user_data.pop('username')
        if instance.user.username != username:
            users = User.objects.filter(username=username)
            if users.count() > 0:
                raise serializers.ValidationError("username already exists.")
        user = User.objects.get_or_create(username=username)[0]
        user.name = user_data['name']
        user.surname = user_data['surname']
        user.email = user_data['email']
        user.tel = user_data['tel']
        user.address = user_data['address']
        user.save()
        instance.user = user
        instance.company_name = validated_data['company_name']
        instance.autoservice_name = validated_data['autoservice_name']
        instance.reg = validated_data['reg']
        instance.vat = validated_data['vat']
        instance.iban = validated_data['iban']
        instance.description = validated_data['description']
        request = self.context.get('request')
        image = request.data['photo_url']
        
        if(type(image) is not str):
            instance.photo_url.save(image.name, image, save=True)
        instance.save()
        return instance

class BusinessUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = BusinessUser
        fields = ( 'url', 'user', 'company_name', 'reg', 'vat')
    
    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        businessuser, created = BusinessUser.objects.update_or_create(user=user,
                            company_name=validated_data.pop('company_name'), 
                            reg=validated_data.pop('reg'), 
                            vat=validated_data.pop('vat'), )
        return businessuser
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        username = user_data.pop('username')
        if instance.user.username != username:
            users = User.objects.filter(username=username)
            if users.count() > 0:
                raise serializers.ValidationError("username already exists.")
        user = User.objects.get_or_create(username=username)[0]
        user.name = user_data['name']
        user.surname = user_data['surname']
        user.email = user_data['email']
        user.tel = user_data['tel']
        user.address = user_data['address']
        user.save()
        instance.user = user
        instance.company_name = validated_data['company_name']
        instance.reg = validated_data['reg']
        instance.vat = validated_data['vat']
        instance.save()

        return instance

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class CarFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFuel
        fields = '__all__'

class CarTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTransmission
        fields = '__all__'



class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceList
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class ServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHistory
        fields = '__all__'
