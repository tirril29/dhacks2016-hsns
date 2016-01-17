from django.shortcuts import render
from django.http import HttpResponse

import models
# Create your views here.



def index(request):
    return render(request, 'app/index.html', {'hackathons': [{'name': x} for x in models.Hackathon.objects.all()]});
    #return HttpResponse("Index Page");


def about(request):
    return render(request,'app/about.html');


def hackathon(request,hackathon_name):
    #render form
    #return render(request,'app/post_template.html',{"user":"Bob Dylan","members":"John Doe","title":"POST TITLE","text":"TEXT"})
    return HttpResponse("ERROROROROROROR %s." % hackathon_name)
