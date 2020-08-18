from django.urls import path, include
from jsonapi import views 
 
urlpatterns = [ 
    path('jsonapi/', views.jsondata_list),
]