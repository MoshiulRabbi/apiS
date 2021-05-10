from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def overview(request):
    data = {
        "message" : "Successful",
        "Predict": "0/1-Test"
    }
    return Response(data)


#Test
@api_view(['POST'])
def predict(request):
    v1 = request.data.get('a')
    return Response(v1)