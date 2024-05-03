from wsgiref.util import request_uri
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

def submitData(request):
    return render(request, 'pg.html')

def demos(request):
    return render(request, 'demo.html')


def s_form(request):
    return render(request, 'reg_form.html')