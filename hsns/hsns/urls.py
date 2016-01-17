"""hsns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/','app.views.about'),

    url(r'^idea/(?P<idea_id>[\d]+)/$','app.views.idea'),
    #url(r'^idea/','app.views.ideaindex'),
    url(r'^ideas/(?P<hackathon_id>[\d]+)/$','app.views.hackathon_idea'),

    url(r'^ad/(?P<ad_id>[\d]+)/$','app.views.ad'),
    #url(r'^ad/','app.views.adindex'),
    url(r'^ads/(?P<hackathon_id>[\d]+)/$','app.views.hackathon_ad'),
    
<<<<<<< HEAD
    url(r'^all_ideas/','app.views.ideaindex'),
    url(r'^all_ads/','app.views.adindex'),
    
    
    url(r'^login/', 'app.views.login'),
    url(r'^logout/', 'app.views.logout'),
    url(r'^register/', 'app.views.register'),
    
    url(r'^$','app.views.index'),
    ]
=======
]
urlpatterns += [
    url(r'^login/', 'app.views.login'),
    url(r'^logout/', 'app.views.logout'),
    url(r'^register/', 'app.views.register')
]
>>>>>>> a1f80a4b36b1b070e7080e71233247e857a97640
