from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import numpy as np

# Create your views here.

@api_view(['GET'])
def overview(request):
    data = {
        "message" : "Avocado Type detection",
        "Predict": "0/1-Test"
    }
    return Response(data)

#test

@api_view(["POST"])
def predict(request):
    try:
        AveragePrice =  request.data.get('AveragePrice',None)
        Total_Volume = request.data.get('Total_Volume',None)
        q_4046 = request.data.get('q_4046',None)
        q_4225 = request.data.get('q_4225',None)
        q_4770 = request.data.get('q_4770',None)
        Total_Bags = request.data.get('Total_Bags',None)
        Small_Bags = request.data.get('Small_Bags',None)
        Large_Bags = request.data.get('Large_Bags',None)
        XLarge_Bags = request.data.get('XLarge_Bags',None)


        fields = [AveragePrice,Total_Volume,
        q_4046,q_4225,q_4770,Total_Bags,Small_Bags,
        Large_Bags,XLarge_Bags]
        
        if not None in fields:

            data = np.array(fields,dtype=float)
            filename = 'ml_model/a_model.pkl'
            avocado_model = pickle.load(open(filename,'rb'))
            prediction = avocado_model.predict([data])

            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction,
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }

    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)