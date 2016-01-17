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
	Hackathon = models.ForeignKey(Hackathon, on_delete = models.CASCADE)
	text = models.CharField(max_length = 1024)
	user = models.ForeignKey(User, related_name = 'member', on_delete = models.CASCADE)
	members = models.ManyToManyField(User)