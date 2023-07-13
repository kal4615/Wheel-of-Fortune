from django.http import HttpResponse
from django.template import loader

def home_page(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def play_page(request):
  template = loader.get_template('play.html')
  return HttpResponse(template.render())