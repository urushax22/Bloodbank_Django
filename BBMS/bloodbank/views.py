from django.http import HttpResponse
from django.template import loader
from .models import Bloodbank

def bloodbank(request):
  donors = Bloodbank.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'donors' : donors,
  }
  return HttpResponse(template.render())

def details(request, id):
  donor = Bloodbank.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'donor' : donor,
  }
  return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
