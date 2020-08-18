from django.db import models
from rest_framework import serializers, viewsets, response
#from djangotoolbox.fields import ListField
# Create your models here.
class Members(models.Model):
    id = models.CharField(max_length=70, blank=False, default='',primary_key=True)
    real_name = models.CharField(max_length=200,blank=False, default='')
    tz = models.CharField(max_length=200,blank=False, default='')

class Period_details(models.Model):
    member = models.ForeignKey(Members, related_name='activity_periods', on_delete=models.CASCADE)
    start_time  = models.DateTimeField(max_length=200,blank=False, default='')
    end_time = models.DateTimeField(max_length=200,blank=False, default='')
    