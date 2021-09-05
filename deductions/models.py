from django.db import models


# Create your models here.

class Deductions(models.Model):
    description = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.description
