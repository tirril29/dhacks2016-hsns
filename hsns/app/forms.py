from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

import models

class Login(forms.Form):
	email_address = forms.EmailField()
	password = forms.CharField()


class Register(forms.Form):
	first_name = Form.CharField(help_text = "Enter your first name. ")
	last_name = Form.CharField(help_text = "Enter your last name. ")
	email_address = Form.EmailField(help_text = "Enter your email address. ")
	password = Form.CharField(help_text = "Enter your totally sercure password. ") # HELLA INSECURE

