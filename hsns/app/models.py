from django.db import models

# Create your models here.
class Hackathon(models.model):
	name = models.CharField(max_length = 30)

class User(models.model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email_address = models.EmailField()
	password = models.CharField(max_length = 30)

class Post(models.model):
	Hackathon = models.ForeignKey(Hackathon)
	text = charfield(1024)
	user = models.ForeignKey(User)
	members = models.ManyToMany(User)