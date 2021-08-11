import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm


def weather(request):
    appid = '1cd32dcfb978b58345d1e2ab96f9cd64'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + \
    appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)


    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/weather.html', context)