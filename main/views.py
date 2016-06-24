from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,Http404,HttpResponse, JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.sites.models import Site
from .forms import *

@csrf_exempt
def mailcyno_admin(request):
	if request.POST:
		body = unicode(u'''
			Name:- %s
			Email:- %s
			Subject:- %s
			Message:- %s
			This is a system generated email. Do Not Reply.
			''') % (request.POST['name'], request.POST['email'], request.POST['subject'], request.POST['message'])
		email = EmailMessage('Get In Touch', body, 'info@cyno.co.in', ['info@cyno.co.in'])
		email.send()
	from .forms import query_form
	return render(request, 'registrations/index.html', {'query_form':query_form})

@csrf_exempt
def career(request):
	if request.POST:
		body = unicode(u'''
			Name:- %s
			Surname:- %s
			Email_id:- %s
			address:- %s
			city:- %s
			postal code:- %s
			country:- %s
			Telephone number:- %s
			Does he/she has a degree:- %s
			degree title:- %s
			institute:- %s
			''') % (request.POST['firstname'], request.POST['lastname'], request.POST['email'], request.POST['address'], request.POST['city'], request.POST['pincode'], request.POST['country'], request.POST['phone'], request.POST['degree'], request.POST['degree_title'], request.POST['institute'])
		email - EmailMessage('apply for career', body, 'hrd@cyno.co.in', ['hrd@cyno.co.in'])
		email.attach_file('''path of resume''')
		email.send()
		from .forms import cv 
		return render(request, 'registrations/index.html', {'cv':cv })