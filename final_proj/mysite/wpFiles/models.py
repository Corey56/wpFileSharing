from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class academic_dept(models.Model):
    dept_code = models.CharField(max_length=10,unique=True)
    dept_name = models.CharField(max_length=100)
    
class academic_class(models.Model):
    class_code = models.CharField(max_length=5,unique=True)
    dept_code = models.ForeignKey(
        academic_dept,
        on_delete=models.CASCADE,
    )
    class_name = models.CharField(max_length=30)
    
class file(models.Model):
    file_alias = models.CharField(max_length=30,unique=True)
    class_code = models.ForeignKey(
        academic_class,
        on_delete=models.CASCADE,
    )
    document = models.FileField(upload_to='documents/')
    rating = models.IntegerField(null=True)
    downloads = models.IntegerField(default=0)
    flags = models.IntegerField
    upload_date = models.DateTimeField(auto_now_add=True)
