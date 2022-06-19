
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from rest_framework import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuoteSerializer



# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    quote = Quote.objects.all().order_by('-created_at')
    serializer = QuoteSerializer(quote,many=True)
    return Response(serializer.data)