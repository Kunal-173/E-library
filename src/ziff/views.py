from django.http import HttpResponse
from django.shortcuts import render


from .forms import RequestForm
from blog.models import Post

def home(Request):
	return render(Request, 'index.html', {'title': 'E-Library : A Study Platform'})

def req(Request):
	#sub = Request.POST['username']
	form = RequestForm(Request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form.save()
		form = RequestForm()
	context={
	'title': 'Request a PDF',
	'form' : form,
	}
	return render(Request, 'request.html', context)

def gate(Request):
	#form.cleaned_data.get('Subject')
	print(Request.GET)
	#qr = RequestForm()
	#sub = qr.Subject
	context = {'title':'GATE', 'sub':''}
	return render(Request, 'gate/content.html', context)	
