from rest_framework import serializers 
from jsonapi.models import All_members
from jsonapi.models import Member
from jsonapi.models import Period
from collections import OrderedDict
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
import json

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('start_time', 'end_time')

class MemberSerializer(serializers.ModelSerializer):
    activity_periods = PeriodSerializer(many=True)
    class Meta:
        model = Member
        fields = ('id','real_name','tz','activity_periods')

class All_MembersSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many =True) 
    class Meta:
        model = All_members
        fields = ('ok','members')

    def create(self, validated_data):
        members = validated_data.pop('members')
        all_members = All_members.objects.create(**validated_data)
        
        for member in members:
            periods = member.pop('activity_periods')
            members_obj = all_members.members.create(**member)
            for p in periods:
                members_obj.activity_periods.create(**p)
        return all_members
