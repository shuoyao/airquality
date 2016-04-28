from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import mcsv,Survey,Response
from django.core.context_processors import csrf
import util
from .forms import NameForm, SurveyForm
# def mform(request):
#     def prepare_blank_answers(survey):
#         for question in Survey.scheme.evaluationquestion_set.all():
#             question.save()

#     evaluation = get_object_or_404(models.Survey)
#     if len(evaluation.evaluationanswer_set.all()) == 0:
#         prepare_blank_answers(evaluation)
#     if request.method == 'POST':
#         formset = forms.AnswerFormSet(request.POST, instance=evaluation)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponse('Thank you!')
#     else:
#         formset = forms.AnswerFormSet(instance=evaluation)
#     return render_to_response('answer_form.html',
#             {'formset':formset, 'Survey':survey})




def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def zipcode(request):
	return render(request, 'zipcode.html')

# def vote(request, question_id):
#     return HttpResponseRedirect(reverse('zipcode', args=(question_id,)))

def fillz(request):
    # if this is a POST request we need to process the form data
    args = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            your_zip = request.POST.get('your_zipcode')
            your_lat,your_lon = util.zipToLatLon(your_zip)
            site_data = util.mostRecentReading(your_lat, your_lon)
        # return HttpResponseRedirect('/polls/zipcode', {'your_lat': your_lat, 'your_lon': your_lon, 'site_data': site_data})
        # return HttpResponseRedirect(reverse('zipcode',  kwargs={'your_lat': your_lat, 'your_lon': your_lon, 'site_data': site_data}))
     
        return render(request, 'zipcode.html', {'your_lat': your_lat, 'your_lon': your_lon, 'site_data': site_data})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, 'detail.html', {'form':form })

def mform(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            newf = form.save()
            qt = request.POST.get('zipcode')
            return render(request, 'surveyform.html', {'qt': qt})
    else: 
        form = SurveyForm()
        # s = Survey.objects.get(pk=2)
        # form = SurveyForm(instance=s)
    args = {}
    args['form'] = form
    return render(request, 'detail.html', {'form':form })
    