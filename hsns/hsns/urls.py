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

    #url(r'^problem/','app.views.option'),
    
    url(r'^login_page/', 'app.views.login_page'),
    url(r'^register_page/', 'app.views.register_page'),
    url(r'^create_page/(?P<type>(True|False))/$', 'app.views.create_page'),

    url(r'^about/','app.views.about'),

    url(r'^idea/(?P<idea_id>[\d]+)/$','app.views.idea'),
    url(r'^ideas/$','app.views.hackathon_idea'),
    #url(r'^ideas/(?P<hackathon_id>[\d]+)/$','app.views.hackathon_idea'),

    url(r'^ad/(?P<ad_id>[\d]+)/$','app.views.ad'),
    url(r'^ads/$','app.views.hackathon_ad'),

    url(r'^all_ideas/','app.views.ideaindex'),
    url(r'^all_ads/','app.views.adindex'),
    #actions
    url(r'^login/', 'app.views.login'),
    url(r'^logout/', 'app.views.logout'),
    url(r'^register/', 'app.views.register'),
    url(r'^create/(?P<type>(True|False))/$', 'app.views.create'),
    url(r'^set/(?P<n>[\d]+)/$', 'app.views.set'),
    
    url(r'^$','app.views.index'),
]

