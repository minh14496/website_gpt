from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    # return HttpResponse('Hello World!')
    
    # render using html
    return render(request, 'hello.html', {'name': 'Minh'})

def index(response):
    
    return render(response, "main/base.html", {})
