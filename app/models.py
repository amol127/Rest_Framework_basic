from django.db import models

# Create your models here.

class Company (models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    about = models.TextField()
    added_data = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 


class Employee(models.Model):
    name= models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    designation = models.CharField(max_length=50,choices=(("Devloper","Devloper"),
                                                          ("tester","tester"),
                                                          ("trainee","trainee"))
                                                          )
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

