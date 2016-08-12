from __future__ import unicode_literals
from django.db import models
class Student1(models.Model):
    father_name=models.CharField(max_length=200)
    mather_name=models.CharField(max_length=200)
    vaccination=models.CharField(max_length=200)
    price=models.CharField(max_length=200)



class Student2(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student1=models.ForeignKey(Student1,on_delete=models.CASCADE)# on_delete using are removes foreignkey  refeanced record.
    auther_name=models.CharField(max_length=200)
    address_name=models.CharField(max_length=200)
    date=models.DateTimeField(max_length=100)





