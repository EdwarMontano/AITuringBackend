from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# Utilities
from datetime import datetime
from itertools import chain
from collections import defaultdict


def pageHome(request):    
    return render(request,'index.html')

def pageNoFound(request):    
    return render(request,'404.html')

def pageBlank(request):    
    return render(request,'blank.html')
