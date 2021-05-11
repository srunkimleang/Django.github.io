from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):#this is going to show title directly not the object of Positon func
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)#(on_delete=models.CASCADE)whenever we delete from Position table then Eployee tabel will also be deleted
