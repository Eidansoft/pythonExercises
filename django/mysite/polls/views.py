# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_questions': latest_questions,
    }

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = 'Esto son los resultados de la encuesta %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('Estas votando la pregunta %s.' % question_id)

