from django.http import HttpResponse
from django.http import JsonResponse
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
    numbers.sort()
    cosas = request.GET['cosas']
    d1 = {"Nombre": "Sara","Edad": 27,"Documento": 1003882,'cursos': ['Python','Django','JavaScript']}
    d1 = {**d1, "number": numbers, "cosas":cosas}
    d2 = {"Nombre": "Tara","Edad": 28,"Documento": 1003883}
    dict3 = defaultdict(list)
    for k, v in chain(d1.items(), d2.items()):       
        dict3[k].append(v)
    # import pdb; pdb.set_trace()
    return JsonResponse(dict3)

def greeting(request,age,name):
    if age >= 18:
        message = 'WELCOME {0}'.format(name)
    else:
        message = 'Sorry {0}, you are not allowed here'.format(name)
    return HttpResponse(message)