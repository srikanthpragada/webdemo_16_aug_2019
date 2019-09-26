from django.shortcuts import render
import requests
import sqlite3
from django.http import HttpResponse


# Create your views here.

def info(request):
    return render(request,'info.html')


def countries_list(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    countries = sorted(countries, key = lambda c : c['population'], reverse=True)[:10]
    return render(request,
                  "countries_list.html",
                  {"countries" : countries} )


