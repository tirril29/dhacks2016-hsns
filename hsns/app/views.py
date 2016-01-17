from django.shortcuts import render
from django.http import HttpResponse

import models
# Create your views here.

def index(request):
    return render(request, 'app/index.html', {'hackathons': [{'name': x['name']} for x in models.Hackathon.objects.all().values('name')]});
    #return HttpResponse("Index Page");

def about(request):
    return render(request,'app/about.html');

#idea and posts are synonyms for the same concept
def idea(request, idea_id):
    
    try:
        idea = get_object_or_404(Word,id=idea_id)
        
        #return render (request,'app/display_ideas.html',{'idea':
                                                             
        return HttpResponse("ALSKDFJALKDSJF - idea %s." % idea_id)
    except:
        return HttpResponse("Nonexistent")

def ideaindex(request, cf = lambda x: True):
    posts = filter(cf, [x for x in models.Post.objects.all().values()])
    #for p in  models.User.object.all():
    #    print p
    return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts]});
    
def hackathon(request,hackathon_name):
    #render form
    return render(request,'app/post_template.html',{"user":"Bob Dylan","members":"John Doe","title":"POST TITLE","text":"TEXT"})

