# voting/views.py

from django.shortcuts import render
from django.http import HttpResponse
import datetime                      
from .models import Voting              


def index(req):
    context = dict(
        all_polls = Voting.objects.all()
    )
    return render(req, 'voting/index.html', context)
    
def one_poll(req, poll_id):
    context = dict(
        the_poll = Voting.objects.get(id=poll_id) 
    )
    return render(req, 'voting/one_poll.html', context)
    

    
