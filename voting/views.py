# voting/views.py

from django.shortcuts import render
from django.http import HttpResponse
import datetime                      
from .models import Voting              


def index(req):
    all_votings = Voting.objects.all()    

    retv = []
    for voting in all_votings:
        retv.append('{}<br />\n'.format(voting.text))

    return HttpResponse(retv) 
    

    
