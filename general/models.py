from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=32, verbose_name="Name")
    surname = models.CharField(max_length=32, verbose_name="Surname")
    email = models.EmailField(verbose_name="Email")
    tel = models.CharField(max_length=15, null=True, verbose_name="Telephone number")
    address = models.CharField(max_length=120, verbose_name="Address")

# Create your models here.
class Merchant(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    company_name = models.CharField(max_length=120, verbose_name="Company Name")
    autoservice_name = models.CharField(max_length=120, verbose_name="Auto Service Name")
    reg = models.IntegerField(verbose_name="Reg")
    vat = models.IntegerField(verbose_name="Vat")
    iban = models.CharField(max_length=120, verbose_name="Iban")
    description = models.TextField(verbose_name="Description")
    photo_url = models.ImageField(verbose_name="Photo", blank=True)
    approved = models.BooleanField(default=False, verbose_name="Approve")

    def __str__(self):
        return self.company_name

class Booking(models.Model):
    book_date = models.DateField(verbose_name="Date")
    merchant = models.ForeignKey('Merchant', on_delete=models.SET_NULL, null=True, verbose_name="Merchant")
    status = models.CharField(max_length=20, verbose_name="Status")

class BusinessUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="User"
    )
    company_name = models.CharField(max_length=32, verbose_name="Company Name")    
    reg = models.IntegerField(verbose_name="Reg")
    vat = models.IntegerField(verbose_name="Vat")

class Chat(models.Model):
    sender = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name="senders", verbose_name="Sender")
    receiver = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name="receivers", verbose_name="Receiver")
    message = models.TextField(verbose_name="Message")
    finished = models.BooleanField(default=False, verbose_name="Finished")

class CarMake(models.Model):
    name = models.CharField(max_length=32)

class CarModel(models.Model):
    name = models.CharField(max_length=32)

class CarFuel(models.Model):
    name = models.CharField(max_length=32)

class CarTransmission(models.Model):
    name = models.CharField(max_length=32)

class CarList(models.Model):
    make = models.ForeignKey('CarMake', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True)
    model_specifiction = models.TextField()
    power = models.FloatField()
    mileage = models.FloatField()
    fuel = models.ForeignKey('CarFuel', on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey('CarTransmission', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()

class Car(models.Model):
    owner = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    car_type = models.ForeignKey('CarList', on_delete=models.SET_NULL, null=True, verbose_name="Car Type")
    vin = models.CharField(max_length=36)
    car_number = models.CharField(max_length=36)

class ServiceList(models.Model):
    merchant = models.ForeignKey('Merchant', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=32)
    price = models.FloatField()
    active = models.BooleanField(default=False,)
    car_make = models.ForeignKey('CarMake', on_delete=models.SET_NULL, null=True)

class Request(models.Model):
    service = models.ForeignKey('ServiceList', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey('CarList', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    answered = models.BooleanField(default=False,)
    answered_date = models.DateField(blank=True)

class ServiceHistory(models.Model):
    request = models.ForeignKey('Request', on_delete=models.SET_NULL, null=True)
    end_date = models.DateField()
    price = models.FloatField()
    details = models.TextField()
    finished = models.BooleanField(default=False,)
    review = models.IntegerField()