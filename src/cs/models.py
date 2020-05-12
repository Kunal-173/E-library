from django.db import models

'''choice = [
('cs','CSE/IT'),
('me','ME'),
('ece','ECE'),
('ee','EE'),
('o','Others'),
]'''

# Create your models here.
class Post(models.Model):
	Subject = models.CharField(max_length=5)