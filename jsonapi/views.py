from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from jsonapi.models import All_members
from jsonapi.models import Member
from jsonapi.models import Period
from jsonapi.serializers import All_MembersSerializer
from jsonapi.serializers import MemberSerializer
from jsonapi.serializers import PeriodSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def jsondata_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        members = All_members.objects.all()
        print(members)
        member_serializer = All_MembersSerializer(members, many=True)
        return JsonResponse(member_serializer.data, safe=False)
        
    elif request.method == 'POST':
        member_serializer = All_MembersSerializer(data=request.data)
    
        print("Neeta")
       
        if member_serializer.is_valid():
            print("BBBB")
            member_serializer.save()
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)