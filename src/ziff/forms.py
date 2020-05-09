from django import forms

from blog.models import Post

choice = [
('cs','CSE/IT'),
('mech','ME'),
('ece','ECE'),
('ee','EE')
]

class RequestForm(forms.ModelForm):
	Name = forms.CharField(max_length=100)
	Email= forms.EmailField(max_length=100)
	Book = forms.CharField(max_length=100)
	Author = forms.CharField(max_length=100)
	Subject = forms.ChoiceField(required=True, label='Choose your stream:-',widget=forms.RadioSelect, choices=choice)
	#add uncommented fields in Meta class and model 
	
	class Meta:
		model = Post
		fields = ['Name',
		'Book',
		'Subject']

	def getStream(self):
		return Subject 
