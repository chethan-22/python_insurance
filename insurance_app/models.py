from django.contrib.auth.models import User as u
from django.db import models



class InsuredMembers(models.Model):
    cust_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    agnt = models.ForeignKey(u, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    dob = models.DateField()

    # def save(self, *args, **kwargs):
    #     self.agnt =
    #     super(InsuredMembers, self).save(*args, **kwargs)

class CustAddress(models.Model):
    cust = models.OneToOneField(InsuredMembers,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)



class Insurances(models.Model):
    types = [('health', 'health insurance'), ('property', 'property insurance'), ('life', 'life insurance')]
    insurance_id = models.AutoField(primary_key=True)
    cust_key = models.OneToOneField(InsuredMembers, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_type = models.CharField(choices=types, max_length=100)






