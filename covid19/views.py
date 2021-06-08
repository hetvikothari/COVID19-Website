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


def get_data():
    url = "https://coronavirus-tracker-india-covid-19.p.rapidapi.com/api/getStatewiseSorted"

    headers = {
        'x-rapidapi-key': "5519f84db3msh5c0859d8c7e62e2p1b1035jsnec618e1be311",
        'x-rapidapi-host': "coronavirus-tracker-india-covid-19.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    data_in_json = json.loads(response.text)
    return data_in_json


def cases(request):
    # url = 'https://www.mohfw.gov.in/data/datanew.json'
    # res = requests.get(url)

    # with open("data.json", "w") as f:
    #     json.dump(res.json(), f)

    data = pd.read_json("https://www.mohfw.gov.in/data/datanew.json")
    # data.drop(['sno', 'state_code'], axis=1, inplace=True)
    # data["Active since Yesterday"] = data['new_active'] - data['active']
    # data["Deaths since Yesterday"] = data['new_death'] - data['death']
    # data["Cured since Yesterday"] = data['new_cured'] - data['cured']
    # data.loc[0, 'state_name'] = 'Andaman & Nicobar Island'
    # data.loc[8, 'state_name'] = 'NCT of Delhi'
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
