from django.http import HttpResponse
from django.shortcuts import render


from .forms import RequestForm
from cs.models import Post

def home(Request):
	return render(Request, 'index.html', {'title': 'E-Library : A Study Platform'})

def req(Request):
	#sub = Request.POST['username']
	sub="null"
	form = RequestForm(Request.POST or None)
	if form.is_valid():
		sub = form.cleaned_data['Subject']
	print(sub)
	return render(Request, 'request.html',{'Subject' : sub, 'form' : form})

def gate(Request):
	#form.cleaned_data.get('Subject')
	#qr = RequestForm()
	#sub = qr.Subject
	sub="cs"
	sub = Request.POST['Subject']
	print(sub)
	if sub == 'cs':
		bg = 'https://c0.wallpaperflare.com/preview/187/633/72/5be997aec83a2.jpg'	
		context = {'title':'GATE', 'sub':'Computer Science and Information Technology', 'bg': bg}
	return render(Request, 'gate/content.html', context)	

def book(request):
	return render(request, 'gate/materials/book.html')

def motivation(request):
	return render(request, 'gate/materials/motivation.html')

def note(request):
	return render(request, 'gate/materials/notes.html')

def pre(request):
	return render(request, 'gate/materials/previous.html')
