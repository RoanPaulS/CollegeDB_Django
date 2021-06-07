from django.db import models

# Create your models here.

class CollegeStudent(models.Model):
    studName = models.CharField(max_length = 30)
    studId = models.IntegerField()
    studDept = models.CharField(max_length = 30)
    studYear = models.CharField(max_length = 30)
