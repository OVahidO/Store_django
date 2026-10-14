from django.shortcuts import render
from django.http import HttpResponse
from store_.models import Customer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def say_hello(request):
    query_set = Customer.objects.all()

    for customer in query_set:
        print(customer)

    return HttpResponse('<html><body><h1>Hello World</h1></body></html>')