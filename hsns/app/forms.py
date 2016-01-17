from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

import models

class Login(forms.Form):
	email_address = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())


class Register(forms.Form):
	first_name = forms.CharField(help_text = "Enter your first name. ")
	last_name = forms.CharField(help_text = "Enter your last name. ")
	email_address = forms.EmailField(help_text = "Enter your email address. ")
	password = forms.CharField(widget=forms.PasswordInput()) # HELLA INSECURE


class Search (forms.Form):
	title_query= forms.CharField(required=False)
	tag_query=forms.CharField(required=False)

class Create(forms.Form):
	title = forms.CharField()
	text = forms.CharField()
	tags = forms.CharField()
	email1 = forms.EmailField(required = False)
	email2 = forms.EmailField(required = False)

