from django.http import HttpResponse
from django.shortcuts import render

def exchange_rate(request):
    return HttpResponse('These are exchange rates')