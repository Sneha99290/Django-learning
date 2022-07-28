from django.http import HttpResponse
from django.shortcuts import HttpResponse

def  index(request):
    return HttpResponse('<h1>Hello World</h1>')

def add(request):
    return HttpResponse('<h2>5+2=7</h1>')

# write a view to return the power of a number  
def power_(request):
    number = request.GET['number']
    number=int(number)
    pow_=number*number
    return HttpResponse(f'<h1>power is {pow_}</h1>')  