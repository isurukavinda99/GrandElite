from django.db import models

# Create your models here.



#salary group model
class SalaryGroup(models.Model):
    grpCode = models.CharField(max_length=20)
    grpAmount = models.FloatField()

    def __str__(self):
        return self.grpCode


#job roles model
class JobRoles(models.Model):
    jobRole = models.CharField(max_length=60)

    def __str__(self):
        return self.jobRole



#employee model
class EmployeeData(models.Model):

    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )

    MARRY = (
        ('Married','Married'),
        ('Unmarried','Unmarried')
    )



    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nic = models.CharField(max_length=10)
    telephone = models.IntegerField(max_length=10)
    email = models.CharField(max_length=60)
    gender = models.CharField(max_length=10,choices=GENDER)
    maritalStatus = models.CharField(max_length=10,choices=MARRY)
    dob = models.DateField()
    profile_pic = models.ImageField(null=True, default='media/def.jpg')
    position = models.ForeignKey(JobRoles,on_delete=models.SET_NULL,null=True)
    basicSalary = models.ForeignKey(SalaryGroup,on_delete=models.SET_NULL,null=True)
    empStatus = models.BooleanField(default=1)
    empAdrs = models.CharField(max_length=100, null=True)
    lastUpdated = models.DateTimeField(auto_now_add=True,null=True)




##############models for attendance management system#########################




class Attendance(models.Model):

    InStatus = (
        ('Absent','Absent'),
        ('On Time','On Time'),
        ('Late', 'Late')
    )

    OutStatus = (
        ('Still Working', 'Still Working'),
        ('On Time', 'On Time'),
        ('Early', 'Early')
    )



    emp_at_id = models.IntegerField
    emp_at_name = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    inTime = models.TimeField(null=True)
    outTime = models.TimeField(null=True)
    inStatus = models.CharField(choices=InStatus, default='Absent', max_length=20)
    outStatus = models.CharField(choices=OutStatus, default='Still Working',max_length=20)

    def __str__(self):
        return self.emp_at_name

