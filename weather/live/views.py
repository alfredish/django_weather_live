from django.shortcuts import render
from django.http import HttpResponse
from .models import City
import requests
from .forms import CityForm

def index(request):
    appid = "e7bd3e1ff50813c8ebed438bf8b64080"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()


    citys = City.objects.all()
    all_cities = []
    for city in citys:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form':form,
    }
    return render(request,'index.html',context)
