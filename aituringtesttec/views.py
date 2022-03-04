from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# Utilities
from datetime import datetime
from itertools import chain
from collections import defaultdict

def helloAlien(request):
    now = datetime.now().strftime(' %Y/%m/%dth, %H:%M')
    return HttpResponse('Hello Mars {now}'.format(now=str(now)))

def sortedNumbers(request):
    numbers = request.GET['numbers'].split(',')
    numbers = [int(n) for n in numbers]
    intSorted=sorted(numbers)
    data = {
        'status':'ok',
        'numbers': intSorted
    }
    
    # import pdb; pdb.set_trace()
    return JsonResponse(data)

def greeting(request,age,name):
    if age >= 18:
        message = 'WELCOME {0}'.format(name)
    else:
        message = 'Sorry {0}, you are not allowed here'.format(name)
    return HttpResponse(message)

