from django.db import models

# Create your models here.
class Hackathon(models.Model):
	name = models.CharField(max_length = 30)

class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email_address = models.EmailField()
	password = models.CharField(max_length = 30)

class Post(models.Model):
	hackathon = models.ForeignKey(Hackathon, on_delete = models.CASCADE)
	type = models.BooleanField()
	title = models.CharField(max_length = 255)
	text = models.CharField(max_length = 1024)
	tags = models.CharField(max_length = 1024)
	user = models.ForeignKey(User, related_name = 'member', on_delete = models.CASCADE)
	members = models.ManyToManyField(User)
	
#Hackathon_id
#text
#user_id
