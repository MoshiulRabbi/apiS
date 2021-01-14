from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.




def home(request):

    if request.method == "POST":
        city = request.POST["location"]

        
        api = "W_API_KEY"
        getweather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

        req = requests.get(getweather)
        res = req.json()

        if res.get('cod')=='404' or city == "":
            return render(request,"weather/home.html",{"err":"Invalid City"})
        else:
            data = res['main']
        #humidity = res.get("wind", dict()).get("speed")
        #icon = res.get("weather", dict()).get("icon")
        return render(request,"weather/home.html",{"weather":data,"city":city})
    else:
        return render(request,"weather/home.html")


def bore(request):
    bore_api = "B_API_KEY"

    req = requests.get(bore_api)
    res = req.json()

    activity = res['activity']
    return render(request,"weather/bore.html",{"activity":activity})