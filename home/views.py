from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    # return HttpResponse('hello Django')
    return render(request, 'index.html')