from django.db import models


# Create your models here.

class SupplierDetails(models.Model):
    supName = models.CharField(max_length=50)
    supEmail = models.EmailField()
    supPhone = models.CharField(max_length=10)
    product = models.CharField(max_length=50)
    amount = models.FloatField()
    status = [
        ('draft', 'Draft'),
        ('paid', 'Paid')
    ]

