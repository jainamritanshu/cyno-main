from django.shortcuts import render

@csrf_exempt
def mailcyno_admin(request):
	if request.POST:
		body = unicode(u'''
			Name:- %s
			Email:- %s
			Telephone:- %s
			Message:- %s
			This is a system generated email. Do Not Reply.
			''') % (request.POST['name'], request.POST['email'], request.POST['phone'], request.POST['message'])
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
			institute:- %s
			Name:- %s
			''') % (request.POST['name'], request.POST['surname'], request.POST['email_id'], request.POST['address'], request.POST['city'], request.POST['post_code'], request.POST['country'], request.POST['telephone'], request.POST['degree'], request.POST['institute'])
		email - EmailMessage('apply for career', body, 'hrd@cyno.co.in', ['hrd@cyno.co.in'])
		email.send()
		from .forms import cv 
		return render(request, 'registrations/index.html', {'cv':cv})