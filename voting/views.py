# voting/views.py

from django.shortcuts import render
from django.http import HttpResponse  # XXX
import datetime                       # XXX


def index(req):
   now = datetime.datetime.now()
   html = 'It is {}'.format(now)
   return HttpResponse(html) 
    

def date(req):
   now = datetime.date.today()
   html = 'It is {}'.format(now)
   return HttpResponse(html) 
    
