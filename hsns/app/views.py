from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect

import models, forms

#Helpers:

loggedin = lambda x: True if 'user' in x and x['user'] is not None else False

login_buttons = [{'name': 'Login', 'type': 'submit', 'action': '/login/'}] #, 'class': 'btn-success'}] 
register_buttons = [{'name': 'Register', 'type':'submit', 'action':'/register/'}]


login_data = {'name': 'Email Address', 'action': '/login/', 'method': 'post', 'button_list': login_buttons} 
register_data = {'name': 'User Name', 'action': '/register/', 'method': 'post', 'button_list': register_buttons} 
#reg_modal = {'id': 'createUser', 'action': '/register/', 'method': 'post', 'title': 'Register User'} 


# Create your views here.
def index(request):
	#print request.session['user']
	hackathons = [{'name': x['name'], 'link': '/set/' + str(x['id'])} for x in models.Hackathon.objects.all().values('id', 'name')]
	return render(request, 'app/index.html', {'logininfo': '1', 'hackathons': hackathons});

def set(request, n):
	request.session['hackathon'] = n;
	return HttpResponseRedirect('/ideas/')

def about(request):
   	return render(request,'app/about.html');

#a page for the information for each 'idea' post
def idea(request, idea_id):
	#return ideaindex(request, cf = lambda x: True if x[u'id'] == idea_id else False)        
        try:
		idea = get_object_or_404(models.Post,id=idea_id)

		return render (request,'app/display_ideas.html',{'idea':idea})
	except:                                                             
		return HttpResponse("Nonexistent Idea")

#gets all ideas from all hackathons
def ideaindex(request):
	#search = request.GET.get('q')
	#titleQ = request.GET.get('t')
	if search == None or titleQ == None:
		search=""
		posts = models.Post.objects.all()
		return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts]});
	posts= models.Post.objects.filter(tags__icontains=search,title__icontains=titleQ)
	if len(posts) == 0:
		return render (request, 'app/ideas_index.html', {'msg': 'No idea fits your search parameter'})
	return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts], 'flag': loggedin(request.session)});

#render ideas for one specific hackathon using hackathon id 
def hackathon_idea(request):#,hackathon_id):
    try:
        #hack = get_object_or_404(models.Hackathon,id=hackathon_id)
        ideasH =  models.Post.objects.filter(hackathon = request.session['hackathon'])
        if len(ideasH) == 0:
            return HttpResponse("No idea has been posted yet")
        return render(request,'app/ideas_index.html',{'idea_list':[x for x in ideasH]});        
        #return render(request,'app/post_template.html',{"hackathon":hack})
    except:
        return HttpResponse("Hackathon not found")

def login_page(request):
	return render(request, 'app/login.html',{'login_data': login_data, 'login_form': forms.Login()})
def register_page(request):
	return render(request, 'app/register.html',{'register_data': register_data, 'register_form': forms.Register()})



##### Group Recruit ######
def ad(request, ad_id):
    try:
        Ad = get_object_or_404(models.Post,id=ad_id)
        
        return render (request,'app/display_ads.html',{'ad':Ad})
    except:                                                             
        return HttpResponse("Nonexistent Ad")

#gets all ads from all hackathons
def adindex(request): #, cf = lambda x: True):
	search = request.GET.get('q')
	if search == None:
		posts = models.Post.objects.all()
		return render (request, 'app/ads_index.html', {'ad_list':[x for x in posts]});
	posts= models.Post.objects.filter(tags__icontains=search)#,title__icontains=search)
	if len(posts) == 0:
		return render (request, 'app/ads_index.html', {'msg': 'No idea fits your search parameter'})
	return render (request, 'app/ads_index.html', {'ad_list':[x for x in posts], 'flag': loggedin(request.session)});
'''    
#posts = filter(cf, [x for x in models.Post.objects.all().values()])
    posts = models.Post.objects.all()
    #for p in  models.User.object.all():
    #    print p
    return render (request, 'app/ads_index.html', {'ad_list':[x for x in posts]});
   ''' 
#render ads for one specific hackathon using hackathon id 
def hackathon_ad(request,hackathon_id):
    try:
        #hack = get_object_or_404(models.Hackathon,id=hackathon_id)
        adsH =  models.Post.objects.filter(hackathon = request.session['hackathon'])
        if len(ideasH) == 0:
            return HttpResponse("No ad has been posted yet")
        return render(request,'app/ads_index.html',{'ad_list':[x for x in adsH]});        
        #return render(request,'app/post_template.html',{"hackathon":hack})
    except:
        return HttpResponse("Hackathon not found")

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
            else:
            	return HttpResponse('No such user.')
    	else:
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
			last_name = form.cleaned_data['last_name']
			email_address = form.cleaned_data['email_address']
			password = form.cleaned_data['password']

			user = models.User.objects.filter(email_address__exact = email_address)
			if len(user) is 0:
				user = models.User(first_name = first_name, last_name = last_name, 
					email_address = email_address, password = password)
				user.save()
				request.session['user'] = user.id
				return HttpResponseRedirect('/')
			else: 
				print "user %s exists" % user[0]
		else:
			print form.errors 
			return HttpResponseRedirect('/')
