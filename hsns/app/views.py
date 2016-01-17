from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import models
# Create your views here.

def index(request):
    return render(request, 'app/index.html', {'hackathons': [{'name': x['name']} for x in models.Hackathon.objects.all().values('name')]});
    #return HttpResponse("Index Page");

def about(request):
    return render(request,'app/about.html');

def idea(request, idea_id):
    try:
        
        idea = get_object_or_404(models.Post,id=idea_id)
        
        return render (request,'app/display_ideas.html',{'idea':idea})
    except:                                                             
        return HttpResponse("Nonexistent")

#gets all ideas from all hackathons
def ideaindex(request, cf = lambda x: True):
    #posts = filter(cf, [x for x in models.Post.objects.all().values()])
    posts = models.Post.objects.all()
    #for p in  models.User.object.all():
    #    print p
    return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts]});
    
#render ideas for one specific hackathon using hackathon id 
def hackathon_idea(request,hackathon_id):
    try:
        hack = get_object_or_404(models.Hackathon,id=hackathon_id)
        ideasH =  models.Post.objects.filter(Hackathon_id = hackathon_id)
        if len(ideasH) == 0:
            return HttpResponse("No idea has been posted yet")
        return render(request,'app/ideas_index.html',{'idea_list':[x for x in ideasH]});        
        #return render(request,'app/post_template.html',{"hackathon":hack})
    except:
        return HttpResponse("Hackathon not found")

##### Group Recruit ######
def ad(request, ad_id):
    try:
        Ad = get_object_or_404(models.Post,id=ad_id)
        
        return render (request,'app/display_ads.html',{'ad':Ad})
    except:                                                             
        return HttpResponse("Nonexistent Ad")

#gets all ads from all hackathons
def adindex(request, cf = lambda x: True):
    #posts = filter(cf, [x for x in models.Post.objects.all().values()])
    posts = models.Post.objects.all()
    #for p in  models.User.object.all():
    #    print p
    return render (request, 'app/ads_index.html', {'ad_list':[x for x in posts]});
    
#render ads for one specific hackathon using hackathon id 
def hackathon_ad(request,hackathon_id):
    try:
        hack = get_object_or_404(models.Hackathon,id=hackathon_id)
        adsH =  models.Post.objects.filter(Hackathon_id = hackathon_id)
        if len(ideasH) == 0:
            return HttpResponse("No ad has been posted yet")
        return render(request,'app/ads_index.html',{'ad_list':[x for x in adsH]});        
        #return render(request,'app/post_template.html',{"hackathon":hack})
    except:
        return HttpResponse("Hackathon not found")
