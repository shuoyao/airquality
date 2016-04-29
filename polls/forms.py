from django import forms
from .models import mcsv,Survey,Response
from django.forms import ModelForm

# class NameForm(forms.Form):
#     your_zipcode = forms.CharField(label='Your zipcode', max_length=100)

# class SurveyForm(ModelForm):
#     class Meta:
#         model = Survey
#         fields = ['question_text']


class NameForm(forms.Form):
    your_zipcode = forms.CharField(label='Your zipcode', max_length=100)

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        # fields = ['question_text']
        fields = '__all__'

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        # fields = ['question_text']
        fields = '__all__'