from django.db import models
import datetime
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating


# Create your models here.
class Academic_dept(models.Model):
    dept_code = models.CharField(max_length=10,unique=True)
    dept_name = models.CharField(max_length=100)
    def __str__(self):
        return self.dept_code
    
class Academic_class(models.Model):
    class_code = models.CharField(max_length=5,unique=True)
    dept_code = models.ForeignKey(
        Academic_dept,
        on_delete=models.CASCADE,
    )
    class_name = models.CharField(max_length=30)
    def __str__(self):
        return self.class_code
    
class Upload(models.Model):
    alias = models.CharField(max_length=30,unique=True)
    class_code = models.ForeignKey(
        Academic_class,
        on_delete=models.CASCADE,
    )
    document = models.FileField(upload_to='documents/')
    rating = GenericRelation(Rating, related_query_name='Files')
    downloads = models.IntegerField(default=0)
    flags = models.IntegerField
    upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.alias 
  

