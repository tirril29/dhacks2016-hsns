from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect

import models, forms

#Helpers:

loggedin = lambda x: True if 'user' in x and x['user'] is not None else False

login_buttons = [{'name': 'Log In', 'type': 'submit', 'action': '/login/'}] #, 'class': 'btn-success'}] 
register_buttons = [{'name': 'Register', 'type':'submit', 'action':'/register/'}]
create_buttons = [{'name': 'Submit', 'type': 'submit', 'action': '/create/'}]


login_data = {'name': 'Log In', 'action': '/login/', 'method': 'post', 'button_list': login_buttons} 
register_data = {'name': 'Register', 'action': '/register/', 'method': 'post', 'button_list': register_buttons} 
create_data = {'name': 'Create', 'action':'/create/', 'method':'post', 'button_list': create_buttons}
#reg_modal = {'id': 'createUser', 'action': '/register/', 'method': 'post', 'title': 'Register User'} 

# Create your views here.
def index(request):
	#print request.session['user']
	hackathons = [{'name': x['name'], 'link': '/set/' + str(x['id'])} for x in models.Hackathon.objects.all().values('id', 'name')]
	return render(request, 'app/index.html', {'logininfo': '1', 'hackathons': hackathons});

def set(request, n):
	request.session['hackathon'] = n;
	return HttpResponseRedirect('/idea/'+n)

def about(request):
   	return render(request,'app/about.html');

#Create and simple log in pages



def create(request, type):
	if request.method == 'POST':
		form = forms.Create(request.POST)
		if form.is_valid():
			hackathon = models.Hackathon.objects.get(id = request.session['hackathon'])
			user = models.User.objects.get(id = request.session['user'])
			type = type
			title = form.cleaned_data['title']
			text = form.cleaned_data['text']
			tags = form.cleaned_data['tags']
			email1 = form.cleaned_data['email1']
			email2 = form.cleaned_data['email2']
			members = [x for x in list(models.User.objects.filter(email_address = email2)) + list(models.User.objects.filter(email_address = email1))]
			post = models.Post(hackathon = hackathon, user = user, type = type,  title = title, text = text, tags = tags)
			post.save()
			for member in members:
				post.members.add(member)
		else:
			print form.errors
			return HttpResponseRedirect('/create_page/' + type + '/')
	return HttpResponseRedirect('/idea/' + str(post.id) if type else '/ad/' + str(post.id))


def login_page(request):
	return render(request, 'app/login.html',{'login_data': login_data, 'login_form': forms.Login()})
def register_page(request):
	return render(request, 'app/register.html',{'register_data': register_data, 'register_form': forms.Register()})
def create_page(request, type):
	c_d = create_data
	c_d['action'] += type + '/'
	return render(request, 'app/create.html', {'create_data': c_d, 'create_form': forms.Create()})


#a page for the information for each 'idea' post
def idea(request, idea_id):
	#return ideaindex(request, cf = lambda x: True if x[u'id'] == idea_id else False)
	idea = get_object_or_404(models.Post,id=idea_id)
	return render (request,'app/display_ideas.html',{'idea':idea})
	try:
		return None;
	except:                                                             
		return HttpResponse("Nonexistent Idea")

#gets all ideas from all hackathons
def ideaindex(request):
	if request.method == "POST":
		form = forms.Search(request.POST)
		if form.is_valid():
			if "submit" in request.POST:
				title_query = form.cleaned_data["title_query"]
				tag_query = form.cleaned_data["tag_query"]
				return HttpResponseRedirect('?q='+tag_query+'&t='+title_query)
		#return render(request,'app/ads_index.html',{'q':tag_query, 't':title_query})
	else:
		form = forms.Search()
		tag_query = request.GET.get('q')
		title_query = request.GET.get('t')
		if title_query == None:
			title_query=""
		if tag_query== None:
			tag_query = ""
		posts= models.Post.objects.filter(tags__icontains=tag_query,title__icontains=title_query)
		if len(posts) == 0:
			return render (request, 'app/ideas_index.html', {'msg': 'No idea fits your search parameter','form':form})
		return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts], 'form':form});

#render ideas for one specific hackathon using hackathon id 
def hackathon_idea(request):#,hackathon_id):
	if request.method == "POST":
		form = forms.Search(request.POST)
		if form.is_valid():
			if "submit" in request.POST:
				title_query = form.cleaned_data["title_query"]
				tag_query = form.cleaned_data["tag_query"]
				return HttpResponseRedirect('?q='+tag_query+'&t='+title_query)
	else:
		form = forms.Search()
		tag_query = request.GET.get('q')
		title_query = request.GET.get('t')
		if title_query == None:
			title_query=""
		if tag_query== None:
			tag_query = ""
		posts= models.Post.objects.filter(tags__icontains=tag_query,title__icontains=title_query,hackathon = request.session['hackathon'])
		if len(posts) == 0:
			return render (request, 'app/ideas_index.html', {'msg': 'No idea fits your search parameter','form':form,'flag': loggedin(request.session)});
		return render (request, 'app/ideas_index.html', {'idea_list':[x for x in posts], 'form':form,'flag': loggedin(request.session)});


#a page for the information for each 'ad' post
def ad(request, ad_id):
	#return adindex(request, cf = lambda x: True if x[u'id'] == ad_id else False)
	ad = get_object_or_404(models.Post,id=ad_id)
	return render (request,'app/display_ads.html',{'ad':ad})
	
def adindex(request): #, cf = lambda x: True)
	if request.method == "POST":
		form = forms.Search(request.POST)
		if form.is_valid():
			if "submit" in request.POST:
				print form.cleaned_data
				print request.POST
				title_query = form.cleaned_data["title_query"]
				tag_query = form.cleaned_data["tag_query"]
				return HttpResponseRedirect('?q='+tag_query+'&t='+title_query)
		#return render(request,'app/ads_index.html',{'q':tag_query, 't':title_query})
	else:
		form = forms.Search()
		tag_query = request.GET.get('q')
		title_query = request.GET.get('t')
		print request.GET
		if title_query == None:
			title_query=""
		if tag_query== None:
			tag_query = ""
		posts= models.Post.objects.filter(tags__icontains=tag_query,title__icontains=title_query)
		print posts
		if len(posts) == 0:
			return render (request, 'app/ads_index.html', {'msg': 'No ad fits your search parameter','form':form,'flag': loggedin(request.session)})
		return render (request, 'app/ads_index.html', {'ad_list':[x for x in posts], 'form':form,'flag': loggedin(request.session)});

#render ads for one specific hackathon using hackathon id 
def hackathon_ad(request):#,hackathon_id):
	if request.method == "POST":
		form = forms.Search(request.POST)
		if form.is_valid():
			if "submit" in request.POST:
				title_query = form.cleaned_data["title_query"]
				tag_query = form.cleaned_data["tag_query"]
				return HttpResponseRedirect('?q='+tag_query+'&t='+title_query)
	else:
		form = forms.Search()
		tag_query = request.GET.get('q')
		title_query = request.GET.get('t')
		if title_query == None:
			title_query=""
		if tag_query== None:
			tag_query = ""
		posts= models.Post.objects.filter(tags__icontains=tag_query,title__icontains=title_query,hackathon = request.session['hackathon'])
		if len(posts) == 0:
			return render (request, 'app/ads_index.html', {'msg': 'No ad fits your search parameter','form':form})
		return render (request, 'app/ads_index.html', {'ad_list':[x for x in posts], 'form':form});

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
	    try:
		    user = models.User.objects.get(email_address__exact = email_address)
            except:
		    return HttpResponseRedirect('/login_page',{'msg':"There is no account associated with this email address."})
	    if user is not None:
                #print "verifying password"
                if user.password == password:
			request.session['username'] = user.first_name
			request.session['user'] = user.id
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/login_page')
	    else:
            	return HttpResponse('No such user.')
    	else:
    		return HttpResponseRedirect('/login_page')

def logout(request):
    """View to Logout of session 

    remove session variables and return to login page 
    """
    request.session['username'] = ""
    request.session['user'] = -1
    for state, sessionInfo in request.session.items():
        sessionInfo = None
	return HttpResponseRedirect('/')
    
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
