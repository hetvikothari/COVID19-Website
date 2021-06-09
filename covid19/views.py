from django.shortcuts import render, HttpResponse, redirect
import requests
import json
import pandas as pd
from .models import Case

# Create your views here.


def index(request):
    return render(request, 'covid19/index.html')


def about(request):
    return render(request, 'covid19/about.html')


def news(request):
    return render(request, 'covid19/news.html')


def protect(request):
    return render(request, 'covid19/protect.html')


def doctors(request):
    return render(request, 'covid19/doctors.html')

def cases(request):
    # url = 'https://www.mohfw.gov.in/data/datanew.json'
    # res = requests.get(url)

    data = pd.read_json("https://www.mohfw.gov.in/data/datanew.json")
    print(data)
    all_obj = Case.objects.all().delete()
    for i in range(1, 36):
        # print(data.iloc[i])
        obj = Case()
        state_name = data.iloc[i][1]
        obj.sno = data.iloc[i][0]
        obj.state_name = data.iloc[i][1]
        obj.active = data.iloc[i][2]
        obj.positive = data.iloc[i][3]
        obj.cured = data.iloc[i][4]
        obj.death = data.iloc[i][5]
        obj.new_active = data.iloc[i][6]
        obj.new_positive = data.iloc[i][7] - data.iloc[i][3]
        obj.new_cured = data.iloc[i][8] - data.iloc[i][4]
        obj.new_death = data.iloc[i][9] - data.iloc[i][5]
        obj.state_code = data.iloc[i][10]
        print(obj)
        obj.save()

    obj = Case.objects.all()

    return render(request, 'covid19/cases.html', {'result': obj})
