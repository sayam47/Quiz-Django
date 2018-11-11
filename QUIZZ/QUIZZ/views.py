from typing import Dict, List, Any, Union

from django.shortcuts import render
from django.http import HttpResponse

totright = int(0)

from website.models import Choice
from . import models

def home(request):
    return HttpResponse('<a href = "login/" >click here to login </a><br><a href="ques/">quiz is here</a>')

def login(request):
    return render(request , 'website/index.html')

def ques(request):
    q=models.Question.objects.get(id=1)
    c=[i for i in q.choices.all()]
    cor=q.choices.get(correct=True).id
    selected_id=0
    global totright
    if request.method == 'POST':
        selected_id=int(request.POST.get('selected'))
        if selected_id == cor:
            totright=totright+1

    context = {
        'question_text' : q.question,
        'choices' : c,
        'correct_id' : cor,
        'selected_id' : selected_id,
        'right' : totright,
    }


    return render(request, 'website/question.html', context)



def ques_id(request,question_id):
    try:
        q=models.Question.objects.get(id=question_id)
    except:
        return HttpResponse("Error 404 Does not exist")
    c=[i for i in q.choices.all()]
    cor=q.choices.get(correct=True).id
    selected_id=0
    global totright
    if request.method == 'POST':
        selected_id=int(request.POST.get('selected'))
        if selected_id == cor:
            totright=totright+1

    context = {
        'question_text' : q.question,
        'choices' : c,
        'correct_id' : cor,
        'selected_id' : selected_id,
        'right' : totright,
    }


    return render(request, 'website/question.html', context)