from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from jsonapi.models import Members
from jsonapi.models import Period_details
#from jsonapi.serializers import All_MembersSerializer
from jsonapi.serializers import MemberSerializer
from jsonapi.serializers import PeriodSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def jsondata_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        members = Members.objects.all()
        print(members)
        member_serializer = MemberSerializer(members, many=True)
        return JsonResponse(member_serializer.data, safe=False)
        
    elif request.method == 'POST':
        member_serializer = MemberSerializer(data=request.data)
    
        print("Neeta")
        print(member_serializer)
        if member_serializer.is_valid():
            member_s = member_serializer.save()
            member_serializer = MemberSerializer(member_s)
            print("AAA")
            print(member_serializer)
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED) 
        
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)