# Create your views here.
from django.shortcuts import render_to_response

import skyguide_calc as calc


def solarsystem(request):
    test_html = calc.test()
    return render_to_response('solarsystem.html', {'results':test_html})