from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    #return render(request, 'template/index.html');
    return HttpResponse("Index Page");


def about(request):
    return render(request,'app/about.html');


def hackathon(request,hackathon_name):
    #render form
    #return render(request,'app/post_template.html',{"user":"Bob Dylan","members":"John Doe","title":"POST TITLE","text":"TEXT"})
    return HttpResponse("ERROROROROROROR %s." % hackathon_name)
