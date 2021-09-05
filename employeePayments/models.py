from django.db import models
import allowances.models
import deductions.models


# Create your models here.
class Employee(models.Model):
    empName = models.CharField(max_length=100, null=True)
    basicWage = models.FloatField(null=True)


class PaySlip(models.Model):
    empID = models.IntegerField(null=True)
    empName = models.CharField(max_length=100, null=True)
    basicWage = models.FloatField(null=True)
    month = models.CharField(max_length=15, null=True)
    allowance = models.ForeignKey(allowances.models.Allowances, on_delete=models.CASCADE)
    deduction = models.ForeignKey(deductions.models.Deductions, on_delete=models.CASCADE)
    netPay = models.FloatField()
