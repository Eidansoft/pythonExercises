# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hola mundo a Django')

def detail(request, question_id):
    return HttpResponse('Esta es la pregunta %s.' % question_id)

def results(request, question_id):
    response = 'Esto son los resultados de la encuesta %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('Estas votando la pregunta %s.' % question_id)

