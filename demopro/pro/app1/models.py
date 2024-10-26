from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class register(models.Model):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=15)
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)

class driverreg(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    profile = models.FileField(upload_to='pdfs')
    cv = models.FileField(upload_to='pdfs')
    phonenumber = models.IntegerField()
    gchoices = (('a',"male"),('b',"female"),)
    gender = models.CharField(max_length=10,choices=gchoices)
    address = models.CharField(max_length=15)
    joiningdate = models.DateField()
    licensenumber = models.CharField(max_length=15)

    location = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    c_password = models.CharField(max_length=10)
    service_status = (
        ('free','free'),
        ('In work', 'In work'),
        ('Off Duty', 'Off Duty'),
    )
    emp_status = models.CharField(max_length=15,choices=service_status,default="free")
    confirmation = (
        ('Pending','Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    c_status = models.CharField(max_length=15,choices=confirmation,default="Pending")

class add_service(models.Model):

    type = models.CharField(max_length=15)
    price = models.IntegerField()
    image =  models.FileField()
class add_location(models.Model):
    location = models.CharField(max_length=100)
    district = models.CharField(max_length=100,default="Ernakulam")
    state = models.CharField(max_length=100, default="Kerala")
class booked(models.Model):
    user_details = models.ForeignKey(register, on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(add_service,on_delete=models.CASCADE,null=True)
    location= models.ForeignKey(add_location,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=15)

    email = models.EmailField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=15)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    pickingdate = models.DateField()
    pickingpoint =  models.CharField(max_length=200)
    quantity = models.IntegerField()
    totalprices = models.FloatField()
    location = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=200, default='Razor_pay', null=True)
class bookings(models.Model):
    user_details = models.ForeignKey(register, on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(add_service,on_delete=models.CASCADE,null=True)
    emp = models.ForeignKey(driverreg, on_delete=models.CASCADE, null=True)
    location= models.ForeignKey(add_location,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=15)

    email = models.EmailField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=15)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    pickingdate = models.DateField()
    pickingpoint =  models.CharField(max_length=200)
    quantity = models.IntegerField()
    totalprices = models.FloatField()
    location = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    service_status = (
        ('Pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=15, choices=service_status,default='pending')
    payment_status = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=200,default='Razor_pay',null=True)
    w_status = models.CharField(max_length=100)






class adminsendbookings(models.Model):
    user_details = models.ForeignKey(register, on_delete=models.CASCADE,null=True)
    emp_details = models.ForeignKey(driverreg, on_delete=models.CASCADE,null=True)

    name = models.CharField(max_length=15)
    email = models.EmailField()
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=15)
    pickingdate = models.DateField()
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    work_confirmation = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    w_confirm = models.CharField(max_length=15, choices=work_confirmation,default='pending')
    work_status = (

        ('Cancelled', 'Cancelled'),
    )
    cl_status = models.CharField(max_length=15, choices=work_status, default='pending')

class cancelbooking(models.Model):
    user_details = models.ForeignKey(register, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(add_service, on_delete=models.CASCADE, null=True)
    emp = models.ForeignKey(driverreg, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(add_location, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=15)

    email = models.EmailField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=15)
    type = models.CharField(max_length=100)
    pickingdate = models.DateField()
    pickingpoint = models.CharField(max_length=200)
    quantity = models.IntegerField()
    totalprices = models.IntegerField()
    location = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    refund_status = (
        ('Pending', 'Pending'),
        ('Refund Initiated', 'Refund Initiated'),

    )
    r_status = models.CharField(max_length=100, choices=refund_status, default='pending')
    payment_status = models.CharField(max_length=100)
    refund_status = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=200, default='Razor_pay', null=True)

class cancelsucces(models.Model):
    user_details = models.ForeignKey(register, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(add_service, on_delete=models.CASCADE, null=True)
    emp = models.ForeignKey(driverreg, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(add_location, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=15)

    email = models.EmailField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=15)
    type = models.CharField(max_length=100)
    pickingdate = models.DateField()
    pickingpoint = models.CharField(max_length=200)
    quantity = models.IntegerField()
    totalprices = models.FloatField()
    location = models.CharField(max_length=100)




class complaint(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
class passwordreset(models.Model):
    users = models.ForeignKey(register, on_delete=models.CASCADE, null=True)
    emp = models.ForeignKey(driverreg, on_delete=models.CASCADE, null=True)
    token=models.CharField(max_length=4)

class finishedworks(models.Model):
    user_details = models.ForeignKey(register, on_delete=models.CASCADE, null=True)
    emp_details = models.ForeignKey(driverreg, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=15)
    email = models.EmailField()
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=15)
    pickingdate = models.DateField()
    city = models.CharField(max_length=50)
    landmark = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

















