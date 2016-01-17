from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import models
# Create your views here.

def index(request):
    return render(request, 'app/index.html', {'hackathons': [x for x in models.Hackathon.objects.all()]});
    #return HttpResponse("Index Page");

def about(request):
    return render(request,'app/about.html');

#idea and posts are synonyms for the same concept
def idea(request, idea_id):
    try:
        idea = get_object_or_404(models.Post,id=idea_id)
        
        return render (request,'app/display_ideas.html',{'idea':idea})
    except:                                                             
        return HttpResponse("Nonexistent")
    
        return HttpResponse("ALSKDFJALKDSJF - idea %s." % idea_id)


def ideaindex(request):
    for y in  models.Post.objects.all():
        print y 
        
    #for p in  models.User.object.all():
    #    print p
    return render (request, 'app/ideas_index.html', {'idea_list':[x for x in models.Post.objects.all()]});
    
def hackathon(request,hackathon_name):
    #render form
    return render(request,'app/post_template.html',{"user":"Bob Dylan","members":"John Doe","title":"POST TITLE","text":"TEXT"})

