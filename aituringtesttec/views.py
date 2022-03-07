from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Utilities
from datetime import datetime
from itertools import chain
from collections import defaultdict

class Inicio(TemplateView):
    template_name='index.html'

def pageHome(request):    
    return render(request,'index.html')

def pageNoFound(request):    
    return render(request,'404.html')

@login_required
def pageBlank(request):    
    return render(request,'blank.html')


def salir(request):
    logout(request)
    return redirect('login')