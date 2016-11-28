# voting/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime                      
from .models import Voting, Answer


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
    
def add_vote(req, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.count += 1
    answer.save()
    return_url =  '/{}/'.format(answer.voting.id)
    return redirect(return_url)
