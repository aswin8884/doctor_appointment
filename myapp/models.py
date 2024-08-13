from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class User_registration(models.Model):

    name=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=250,null=True)
    contact=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    profile_picture=models.ImageField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)

class Add_doctors(models.Model):

    name=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=250,null=True)
    contact=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    qualification=models.CharField(max_length=250,null=True)
    experience=models.CharField(max_length=250,null=True)
    hospital=models.CharField(max_length=100,null=True)
    specialization=models.CharField(max_length=250,null=True)
    description=models.CharField(max_length=500,null=True)
    profile_picture=models.ImageField(null=True)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)


class Add_appointment(models.Model):

    doctor_id=models.ForeignKey(Add_doctors,on_delete=models.CASCADE,null=True)
    fees=models.CharField(max_length=25,null=True)
    appointment_time_from=models.TimeField(null=True)
    appointment_time_to=models.TimeField(null=True)
    appointment_date=models.DateField(null=True)
    user_booked=models.BooleanField(default=False)

class Booking_slote(models.Model):

    slote_id=models.ForeignKey(Add_appointment,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=25,null=True)
    number=models.IntegerField(null=True)
    transaction=models.BooleanField(default=False)
    user_booked=models.BooleanField(default=False)
    payment_date=models.DateTimeField(null=True)

class Add_complaints(models.Model):

    title=models.CharField(max_length=50,null=True)
    complaint=models.CharField(max_length=500,null=True)
    posted_date=models.DateTimeField(null=True)
    admin_reply=models.CharField(max_length=500,default="pending")
    reply_date=models.DateTimeField(null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    doctor_id=models.ForeignKey(Add_doctors,on_delete=models.CASCADE,null=True)

class Add_feedbacks(models.Model):

    title=models.CharField(max_length=50,null=True)
    feedback=models.CharField(max_length=500,null=True)
    rating=models.IntegerField(null=True)
    posted_date=models.DateTimeField(null=True)
    user_id=models.ForeignKey(User_registration,on_delete=models.CASCADE,null=True)
    doctor_id=models.ForeignKey(Add_doctors,on_delete=models.CASCADE,null=True)
    





    