from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

import models

class Login(forms.Form):
	email_address = forms.EmailField()
	password = forms.CharField()
	user = models.Users.objects.get(email_address__exact = email_address)
	if user == None:
		raise Exception('No such email exists. ')
		return
	elif user.password != password:
		raise Exception('Wrong Password. ')
	else:
		request.session['user'] = user.id


class Register(forms.Form):
	first_name = Form.CharField(help_text = "Enter your first name. ")
	last_name = Form.CharField(help_text = "Enter your last name. ")
	email_address = Form.EmailField(help_text = "Enter your email address. ")

	if len([models.User.objects.filter(email_address__exact = email_address)]) > 0:
		raise Exception('Email Already exists.')

	password = Form.CharField(help_text = "Enter your totally sercure password. ") # HELLA INSECURE

	def save(self, force_insert=False, force_update=False, commit=True):
		new_user = super(Register, self).save(commit = False)
		new_user = models.User(first_name = self.first_name, last_name = self.last_name, 
			email_address = self.email_address, password = self.password)

		if commit:
			new_user.save()

		request.session['user'] = user.id

		return new_user


