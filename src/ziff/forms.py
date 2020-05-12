from django import forms

from cs.models import Post

choice = [
('cs','CSE/IT'),
('mech','ME'),
('ece','ECE'),
('ee','EE'),
('o','Other'),
]

class RequestForm(forms.Form):
	Subject = forms.ChoiceField(required=True, label='Choose your stream ',widget=forms.RadioSelect, choices=choice)
	#add uncommented fields in Meta class and model 
	
	#class Meta:
		#model = Post
		#fields = ['Subject',
		#	]

