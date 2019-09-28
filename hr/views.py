from django.shortcuts import render
import requests
from .forms import InterestForm
import sqlite3
from django.http import HttpResponse


# Create your views here.

def info(request):
    return render(request, 'info.html')


def countries_list(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    countries = sorted(countries, key=lambda c: c['population'], reverse=True)[:10]
    return render(request,
                  "countries_list.html",
                  {"countries": countries})


def interest(request):
    if request.method == "GET":
        f = InterestForm()
        return render(request, 'interest.html', {'form': f})
    else:
        f = InterestForm(request.POST)
        interest = None
        if f.is_valid():
            amount = f.cleaned_data['amount']
            rate = f.cleaned_data['rate']
            interest = amount * rate / 100

        return render(request, 'interest.html',
                      {'form': f, 'interest': interest})
