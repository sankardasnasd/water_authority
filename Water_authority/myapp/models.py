from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class District(models.Model):
    Dis_name=models.CharField(max_length=100)

class Area(models.Model):
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    Place=models.CharField(max_length=100)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    AREA = models.ForeignKey(Area, on_delete=models.CASCADE, default=1)
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Dob=models.CharField(max_length=100)
    Panchayath=models.CharField(max_length=100)
    Pincode=models.CharField(max_length=100)
    Photo=models.CharField(max_length=300)
    Email=models.CharField(max_length=100)
    Village=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    ConnectionsStatus=models.CharField(max_length=100)

class Meterreader(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Dob=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    Pincode=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)



class Assign_meter_reader(models.Model):
    METRERREADER=models.ForeignKey(Meterreader,on_delete=models.CASCADE,default=1)
    AREA=models.ForeignKey(Area,on_delete=models.CASCADE,default=1)


class Notification(models.Model):
    Date=models.DateField()
    Notification=models.CharField(max_length=100)

class Usage(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Date=models.DateField()
    Year=models.CharField(max_length=100)
    Month=models.CharField(max_length=100)
    Usage=models.FloatField(max_length=100)
    Amount=models.CharField(max_length=100)
    Payment_status=models.CharField(max_length=100)
    Type=models.CharField(max_length=100,default="Monthly Bill")


class Userupload(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Date=models.DateField()
    Photo=models.CharField(max_length=100)

class Charges(models.Model):
    Fromunit=models.FloatField(max_length=100)
    Tounit=models.FloatField(max_length=100)
    Amount=models.CharField(max_length=100)

class Complaint(models.Model):
    FROM=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    TO=models.ForeignKey(Meterreader,on_delete=models.CASCADE,default=1)
    Date=models.DateField()
    Complaint=models.CharField(max_length=100)
    Reply=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)

class Payment(models.Model):
    REQUESTID=models.ForeignKey(Usage,on_delete=models.CASCADE,default=1)
    Date=models.DateField()
    Amount=models.CharField(max_length=100)

class Public(models.Model):
    Date=models.DateField()
    Complaint=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Bank(models.Model):
    Accno=models.CharField(max_length=100)
    Ifsc=models.CharField(max_length=100)
    Balance=models.CharField(max_length=100)
    Cvv=models.CharField(max_length=100)
