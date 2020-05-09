from django.db import models

'''
choice = [
('cs','CSE/IT'),
('mech','ME'),
('ece','ECE'),
('ee','EE')
]'''

# Create your models here.
class Post(models.Model):
	Name = models.CharField(max_length=100)
	Email= models.EmailField(max_length=100)
	Book = models.CharField(max_length=100)
	Author = models.CharField(max_length=100)
	Subject = models.CharField(max_length=5)