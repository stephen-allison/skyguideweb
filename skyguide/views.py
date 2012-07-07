# Create your views here.
from django.shortcuts import render_to_response

import skyguide_calc as calc

def solarsystem(request):
    return render_to_response('solarsystem.html')