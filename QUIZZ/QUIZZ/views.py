from typing import Dict, List, Any, Union
from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    return HttpResponse('<a href = "login/" >click here to login </a><br><a href="ques/">quiz is here</a>')

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name='signup.html'

def login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))