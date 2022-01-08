from django.shortcuts import render
from django.http import HttpResponse

import urllib.request
import json

# Create your views here.
def index(request):
    return HttpResponse('HELLO')