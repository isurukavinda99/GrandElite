from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200 , unique=True , null=False , blank=False)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='isms/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name

class Supplier(models.Model):

    name = models.CharField(max_length=200 , null=False , blank=False)
    email = models.EmailField(max_length=200 , null=False , blank=False , unique=True)
    phone = models.CharField(max_length=10 , null=False , blank=False , validators=[MinLengthValidator(10)])
    address = models.TextField(null=False , blank=False)
    nic = models.CharField(max_length=9 , unique=True , blank=False , null=False , validators=[MinLengthValidator(9)])
    br_number = models.CharField(max_length=5 , unique=True , null=False , blank=False)

    # items = models.ManyToManyField(Item , null=True , blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Item(models.Model):

    name = models.CharField(max_length=200 , unique=True , blank=False , null=False)
    description = description = models.TextField()
    quantity = models.FloatField(null=False , blank=False)
    notify_level = models.FloatField(null=False , blank=False)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=False)
    suppliers = models.ManyToManyField(Supplier , null=True , blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SendMail(models.Model):

    email_body = models.TextField()
    items = models.ManyToManyField(Item , related_name="ordered_items")
    suppliers = models.ManyToManyField(Supplier , related_name="request_suppliers")
    quantity = models.ImageField()
    request_date = models.DateTimeField(auto_now_add=True)