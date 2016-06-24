from django.forms import forms

class query_form(forms.Form):
	Name = forms.CharField(label = 'Your name', max_length = 100)
	Email = forms.CharField(label = 'Email Id', max_length = 50)
	Telephone = forms.IntegerField(label = 'Telephone number')
	Message = forms.CharField(label = 'Your query', max_length = 500)

class cv(forms.Form):
	Name = forms.CharField(label = 'First Name', max_length = 100)
	Surname = forms.CharField(label = 'Last Name', max_length = 100)
	Email_id = forms.EmailField(label = 'Email id', max_length = 100)	
	address = forms.CharField(label = 'address', max_length = 500)
	city = forms.CharField(label = 'city', max_length = 100)
	post_code = forms.IntegerField(label = 'postal code')
	country = forms.CharField(label = 'Country', max_length = 100)
	Telephone = forms.IntegerField(label = 'Telephone number')
	h_deg = forms.CharField(label = 'Do you have a degree', max_length = 100)
	insti = forms.CharField(label = 'Where did you complete you degree', max_length = 100)
	cv = forms.FileField(upload_to = #file path tbd)