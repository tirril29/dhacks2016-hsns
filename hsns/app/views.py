from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    #return render(request, 'template/index.html');
    return HttpResponse("Index Page");


def hackathon(request):
    return render(request,'app/about.html',context="");
    return HttpResponse("About Page");
