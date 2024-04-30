from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_info(request):
    return HttpResponse('Enter the name of the product you want to buy: ')