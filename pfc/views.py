from django.http import HttpResponse
from django.template import loader
from .models import *
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
  
def static_about(request):
  template = loader.get_template('static_about.html')
  return HttpResponse(template.render())

def static_become_foster(request):
  template = loader.get_template('static_become_foster.html')
  return HttpResponse(template.render())

def static_contact(request):
  template = loader.get_template('static_contact.html')
  return HttpResponse(template.render())

def static_faq(request):
  template = loader.get_template('static_faq.html')
  return HttpResponse(template.render())

def static_gdpr(request):
  template = loader.get_template('static_gdpr.html')
  return HttpResponse(template.render())

def static_legal(request):
  template = loader.get_template('static_legal.html')
  return HttpResponse(template.render())

def static_map(request):
  template = loader.get_template('static_map.html')
  return HttpResponse(template.render())


def signin_foster(request):
  template = loader.get_template('signin_foster.html')
  return HttpResponse(template.render())

def signin_shelter(request):
  template = loader.get_template('signin_shelter.html')
  return HttpResponse(template.render())

def signin_login(request):
  template = loader.get_template('signin_login.html')
  return HttpResponse(template.render())

""" Models needed from here on """

def animal_list(request):
  animals = Animal.objects.all()
  species = Espece.objects.all()
  tags = Tag.objects.all()
  template = loader.get_template('animal_list.html')
  context = {
    'animals': animals,
    'especes': species,
    'tags': tags
  }
  return HttpResponse(template.render(context, request))

def animal_details(request, animalId):
  animal = Animal.objects.get(id=animalId)
  template = loader.get_template('animal_details.html')
  context = {
    'animal': animal,
  }
  return HttpResponse(template.render(context, request))

def shelter_list(request):
  shelters = Association.objects.all()
  species = Espece.objects.all()
  tags = Tag.objects.all()
  template = loader.get_template('shelter_list.html')
  context = {
    'associations': shelters,
    'especes': species,
    'tags': tags
  }
  return HttpResponse(template.render(context, request))

def shelter_details(request, shelterId):
  shelter = Association.objects.get(id=shelterId)
  template = loader.get_template('shelter_details.html')
  context = {
    'association': shelter,
  }
  return HttpResponse(template.render(context, request))

""" Connected routes go here """