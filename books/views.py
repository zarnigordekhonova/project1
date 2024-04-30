from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_book_name(request):
    return HttpResponse('Enter the book title you want to buy: ')