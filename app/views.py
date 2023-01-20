from django.shortcuts import render
from django. http import HttpResponse
# Create your views here.
def abc(request,malli):
    return HttpResponse('</h1>work is worship</h1>{}'.format(malli))