from django.db import models
from rest_framework import serializers, viewsets, response

class All_members(models.Model):
    ok = models.CharField(max_length=70, blank=False, default='')

# Member class is the table which is containing all members list.
class Member(models.Model):
    id = models.CharField(max_length=70, blank=False, default='',primary_key=True)
    real_name = models.CharField(max_length=200, blank=False, default='')
    tz = models.CharField(max_length=200,blank=False, default='')
    members = models.ForeignKey(All_members, related_name='members', on_delete=models.CASCADE)

#Period class is the table which is containing all activity period list for each member.
class Period(models.Model):
    member = models.ForeignKey(Member, related_name='activity_periods', on_delete=models.CASCADE)
    start_time  = models.DateTimeField(max_length=200,blank=False, default='')
    end_time = models.DateTimeField(max_length=200,blank=False, default='')
