from django import forms
from models import Question
from models import Choice

class NameForm(forms.Form):
	class Meta:
		modelq = Question
		modelc = Choice
		fields = ('c1','c2','c3','sub')

  