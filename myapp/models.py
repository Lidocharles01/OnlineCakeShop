from django.db import models

#user_login,user_details,cake_master,cake_order,cake_payment

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


class cake_master(models.Model):
    name  = models.CharField(max_length=50)
    description  = models.CharField(max_length=500)
    qty  = models.CharField(max_length=50)
    price  = models.CharField(max_length=50)
    pic = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class cake_order(models.Model):
    user_id = models.IntegerField()
    cake_id = models.IntegerField()
    dt  = models.CharField(max_length=50)
    tm  = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    bdt = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class cake_payment(models.Model):
    user_id = models.IntegerField()
    cake_id = models.IntegerField()
    amt = models.CharField(max_length=50)
    card_no = models.CharField(max_length=50)
    cvv  = models.CharField(max_length=50)
    dt  = models.CharField(max_length=50)
    tm  = models.CharField(max_length=50)
    status = models.CharField(max_length=50)