from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    stud_class=models.CharField(max_length=40)
    department=models.CharField(max_length=40)