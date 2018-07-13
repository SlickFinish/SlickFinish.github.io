from django.shortcuts import render

def index(request):
	return render( request,'index/index.html')

def contact(request):
	return render ( request, 'index/about.html')

def work(request):
	return render (request, 'index/services.html')

def connect(request):
	return render (request, 'index/contact.html')
	