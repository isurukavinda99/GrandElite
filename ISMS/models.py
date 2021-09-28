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

    status_choices = [
        ('requested' , 'Requested'),
        ('suppler_confirmed' , 'Suppler confirmed')
    ]

    email_body = models.TextField()
    items = models.ForeignKey(Item , related_name="ordered_items" , on_delete=models.DO_NOTHING , null=False , blank=False)
    suppliers = models.ManyToManyField(Supplier , related_name="request_suppliers")
    quantity = models.IntegerField()
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200 ,null=True , blank=True , default="requested" ,choices=status_choices)

    def __str__(self):
        return  str(self.id) + ' - ' + self.status + ' - ' + self.items.name

class ItemReleaseTicket(models.Model):

    item = models.ForeignKey(Item , related_name='release_item' , on_delete=models.DO_NOTHING , null=False)
    released_to = models.CharField(max_length=100 , null=False , blank=False)
    released_quantity = models.IntegerField(null=False , blank=False)
    current_quantity = models.IntegerField(null=False , blank=False)
    released_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.item.name + ' - ' + self.released_to + ' - ' + str(self.released_quantity) + ' - ' + str(self.released_date)


class ConfirmedInvoice(models.Model):

    status_choices = [
        ('pending' , 'Pending'),
        ('payment_done' , 'Payment done')
    ]

    emailRequest = models.OneToOneField(SendMail , on_delete=models.CASCADE , null=False)
    offered_price = models.FloatField(null=False)
    status = models.CharField(null=True , blank=True , choices=status_choices , default="pending" , max_length=200)
    invoice_to = models.ForeignKey(Supplier , on_delete=models.CASCADE , null=True , blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)