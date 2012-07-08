# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpRequest


import skyguide_calc as calc
import json


def solarsystem(request):
    test_html = calc.test()
    return render_to_response('solarsystem.html', {'results':test_html})

def solarsystem_json(request):
    data = calc.get_solar_system_body_properties()
    json_data = json.JSONEncoder().encode(data)
    return HttpResponse(json_data, 'application/json')


def client(request):
    return render_to_response('client.html')