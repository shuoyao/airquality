from django import forms

class NameForm(forms.Form):
    your_zipcode = forms.CharField(label='Your zipcode', max_length=100)
   #  your_lat = forms.CharField(label='Your lat', max_length=100)
   # your_lon  = forms.CharField(label='Your lon', max_length=100)
