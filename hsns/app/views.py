from django.shortcuts import render
from django.http import HttpResponse

import models
# Create your views here.



def index(request):
    return render(request, 'templates/index.html', {'hackathons': [{'name': x} for x in models.Hackathon.objects.all()]});
    #return HttpResponse("Index Page");


def hackathon(request):
    return render(request,'app/about.html',context="");
    return HttpResponse("About Page");
