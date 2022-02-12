from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Url
import uuid

# Create your views here.
def index(request):
	return render(request, 'index.html')

def shorten(request):
	if request.method == 'POST':
		link = request.POST['link']
		uid = str(uuid.uuid4())[:6]
		if ('https://' not in link and 'http://' not in link):
			link = 'https://' + link
		# Creating new shortened URL
		new_url = Url(link=link, uuid=uid)
		new_url.save()
		return HttpResponse(uid)
	messages.info(request, 'Oops, no URL found. Looks like you have entered the wrong link.')
	return redirect('/')
	# HttpResponse will be sent to Ajax

def go(request, uuid):
	# Django admin panel won't be able to be accessed through '/admin'
	# Change path in urls.py for admin site
	if Url.objects.filter(uuid=uuid).exists():
		return redirect(Url.objects.get(uuid=uuid).link)
	messages.info(request, 'Oops, no URL found. Looks like you have entered the wrong link.')
	return redirect('/')

def dump(request, re):
	messages.info(request, 'Oops, no URL found. Looks like you have entered the wrong link.')
	return redirect('/')