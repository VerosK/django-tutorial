# voting/views.py

from django.shortcuts import render
from django.http import HttpResponse
import datetime                      
from .models import Voting              


def index(req):
    all_votings = Voting.objects.all()    

    retv = []
    for voting in all_votings:
        retv.append('''
            <a href="/{}/">{}</a><br />
            '''.format(voting.id, voting.text))

    return HttpResponse(retv) 
    
def one_poll(req, poll_id):

    a_poll = Voting.objects.get(id=poll_id)    
    retv = ''' <h1>{}</h1> '''.format(a_poll.text)

    return HttpResponse(retv)
    

    
