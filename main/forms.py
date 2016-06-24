from django.forms import forms
import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class query_form(forms.Form):
	Name = forms.CharField(label = 'Your name', max_length = 100)
	Email = forms.CharField(label = 'Email Id', max_length = 50)
	Subject = forms.IntegerField(label = 'Telephone number')
	Message = forms.CharField(label = 'Your query', max_length = 500)

class cv(forms.Form):
	boole =(
			('Yes', 'Yes'),
			('No', 'No'),
		) 


	Name = forms.CharField(label = 'First Name', max_length = 100)
	Surname = forms.CharField(label = 'Last Name', max_length = 100)
	Email_id = forms.EmailField(label = 'Email id', max_length = 100)	
	address = forms.CharField(label = 'address', max_length = 500)
	city = forms.CharField(label = 'city', max_length = 100)
	post_code = forms.IntegerField(label = 'postal code')
	country = forms.CharField(label = 'Country', max_length = 100)
	Telephone = forms.IntegerField(label = 'Telephone number')
	h_deg = forms.ChoiceField(widget=forms.RadioSelect(attrs={ 'required': 'true' }), choices=boole)
	insti = forms.CharField(label = 'Where did you complete you degree', max_length = 100)
	w_deg = forms.CharField(label = 'Degree title', max_length = 100)
	cv = forms.FileField(upload_to = #file path tbd)

