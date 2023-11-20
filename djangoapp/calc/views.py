from django.shortcuts import render
from django.http import HttpResponse

# hello/?x=10
# def hello(request):
#     return HttpResponse(f"Hello World! {request.GET['x']}")

# hello/10
def hello(request, number):
    return HttpResponse(f"Hello World! {number}")

def calc(request):
    pass