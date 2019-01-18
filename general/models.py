from django.db import models

# Create your models here.
class Merchant(models.Model):
    company_name = models.CharField(max_length=120)
    name = models.CharField(max_length=32)
    surename = models.CharField(max_length=32)
    email = models.EmailField()
    autoservice_name = models.CharField(max_length=120)
    reg = models.IntegerField()
    vat = models.IntegerField()
    tel = models.CharField(max_length=15, null=True, help_text="Telephone number")
    address = models.CharField(max_length=120)
    iban = models.CharField(max_length=120)
    description = models.TextField()
    photo_url = models.ImageField(upload_to='photos/')
    approved = models.BooleanField()

    def __str__(self):
        return self.company_name