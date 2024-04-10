from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm

def registerPage(request):
  form= UserCreationForm()
  context={'form':form}
  return render (request,'register.html', context)
def loginPage(request):
  context={}
  return render (request,'login.html', context)





