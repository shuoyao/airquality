from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import mcsv,Survey,Response
from django.core.context_processors import csrf
from . import util
from .forms import NameForm, SurveyForm, ResponseForm
from django.forms.widgets import HiddenInput

def index(request):
    return render(request, 'index.html')

def zipcode(request):
    return render(request, 'zipcode.html')

def prob(request):
    return render(request, 'quality-problem.html')

def fillz(request):
    # if this is a POST request we need to process the form data
    args = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            your_zip = request.POST.get('your_zipcode')
            your_lat, your_lon, state_data = util.zipToLatLonState(your_zip)
            site_data = util.mostRecentReading(your_lat, your_lon)
        #TODO: Is passing lat and long necessary?
        return render(request, 'zipcode.html', {'your_lat': your_lat,
                                                'your_lon': your_lon,
                                                'state_data': state_data,
                                                'site_data': site_data,
                                                'zipcode':your_zip})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return render(request, 'detail.html', {'form':form })

def mform(request,zid):
    if request.method == 'POST':
        rform = ResponseForm(request.POST)
        ctxt = {}
        if rform.is_valid():
            newf = rform.save()
            #TODO: Is this get and context necessary?
            ctxt = {}
            ctxt['zip'] = request.POST.get('zipcode')
            email = request.POST.get('email_or_not')
            if email == '1':
                ctxt['email'] = email
            return render(request, 'thanks.html', ctxt)
    rform = ResponseForm(initial={'zipcode':zid})
    rform.fields['zipcode'].widget = HiddenInput()
    questions = Survey.objects.all()
    args = {}
    args['rform'] = rform
    args['questions'] = questions
    return render(request, 'surveyform.html', args)
