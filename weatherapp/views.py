from django.shortcuts import render
import requests
import datetime


# Create your views here.
def index(request):
    if 'city' in request.POST:
        q=request.POST['city']
    else:
        q='tehran'
    appid='6ad934a76186d5d2fb596a8e925a0cae'
    url='https://api.openweathermap.org/data/2.5/weather'
    units='metric'
    params={'q':q,'appid':appid,'url':url,'units':units}
    r=requests.get(url=url,params=params).json()  # web scraping 
    description=r['weather'][0]['description']
    icon=r['weather'][0]['icon']
    temp=r['main']['temp']
    humidity=r['main']['humidity']
    day=datetime.date.today()
    return render(request, "weatherapp/index.html", {'description':description,'temp':temp,'humidity':humidity,'q':q,'icon':icon,'day':day})
