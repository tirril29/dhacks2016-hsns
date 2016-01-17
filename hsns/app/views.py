from django.shortcuts import render
from django.http import HttpResponse

import models

#Helpers:

login_buttons = [{'name': 'Login', 'type': 'submit', 'action': '/login/'}, #, 'class': 'btn-primary'},
{'name': 'Register', 'type': 'modal', 'data_target': '#createUser'}] #, 'class': 'btn-success'}] 


login_data = {'name': 'User Name', 'action': '/login', 'method': 'post', 'button_list': login_buttons} 

reg_modal = {'id': 'createUser', 'action': '/register', 'method': 'post', 'title': 'Register User'} 


# Create your views here.
def index(request):
	hackathons = [{'name': x['name']} for x in models.Hackathon.objects.all().values('name')]
	return render(request, 'app/index.html', {'hackathons': hackathons, 'login_data': login_data, 'login_form': forms.Login(), 
                  'reg_modal': reg_modal, 'reg_form': forms.Register()});
    #return HttpResponse("Index Page");

def about(request):
   	return render(request,'app/about.html');

#idea and posts are synonyms for the same concept
def idea(request, idea_id):
	return ideaindex(request, cf = lambda x: True if x[u'id'] == idea_id else False)

def ideaindex(request, cf = lambda x: True):
	posts = filter(cf, [x for x in models.Post.objects.all().values()])
	return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts]});

def hackathon(request,hackathon_name):
    #render form
    return render(request,'app/post_template.html',{"user":"Bob Dylan","members":"John Doe","title":"POST TITLE","text":"TEXT"})

################
## FORM VIEWS ##
################

### User Actions ###
def login(request):
    """View to Login a user
    
    Checks post credentials, redirects
    to projects or back to front page with error 
    """
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            #print "form is valid"
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            user = models.User.objects.get(email_address__exact = email_address)
            if user is not None:
                #print "verifying password"
                if user.password == password:
                    request.session['user'] = user.id
                    return HttpResponseRedirect('/')

def logout(request):
    """View to Logout of session 

    remove session variables and return to login page 
    """
    for state, sessionInfo in request.session.items():
        sessionInfo = None
	return HttpResponseRedirect('/')

## STILL EXISTS BECAUSE OWEN IS WORKING ON LOGIN PAGE 
## I DON'T WANT TO RESTRUCTURE REG FORMS, WILL BE Create_Object
def register(request):
    if request.method == "POST":
        form = forms.Register(request.POST)
        if form.is_valid():
        	first_name = form.cleaned_data['first_name']
        	last_name =  = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            password = form.cleaned_data['password']

            user = models.User.objects.get(email_address__exact = email_address)
            if user is None:
                user = models.User(first_name = first_name, last_name = last_name, 
                	email_address = email_address, password = password)
                user.save()
                request.session['user'] = user.id
                return HttpResponseRedirect('/')
            else:
                print "user %s exists" % user
        else:
            print form.errors 
    return HttpResponseRedirect('/')
