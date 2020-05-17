from django.db import models

class Employee(models.Model):
    employee_id=models.CharField(max_length=10, primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile_no=models.IntegerField()
    city=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Company(models.Model):
    job_profile_id=models.CharField(max_length=100)
    job_profile=models.CharField(max_length=100)
    salary=models.IntegerField()
    employee_id=models.CharField(max_length=10 ,primary_key=True)
    def __str__(self):
        return self.job_profile
    
