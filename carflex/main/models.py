from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Car(models.Model):
    category = models.CharField(max_length=100,blank=True,null=True)
    make = models.CharField(max_length=100,blank=True,null=True)
    model = models.CharField(max_length=100, blank=True,null=True)
    year = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(blank=True,null=True, upload_to='images')
    is_available = models.BooleanField(default=True)
    license_plate = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f"{self.make}+' '+{self.models}+' '+{self.model}"

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.BigIntegerField(unique=True)
    tel_number =  models.IntegerField(unique=True)
    address = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.user}"

class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10,decimal_places=10,blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.total_price:
            duration = (self.end_date-self.start_date).days
            self.total_price = duration * self.total_price
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Resrevation for {self.car} for {self.user} from {self.start_date} to {self.end_date}"