from django.http import HttpResponse
from django.template import loader
from .models import *
from django.db.models import Q
import operator
from functools import reduce
  
def main(request):
  template = loader.get_template('main.html')
  animals = Animal.objects.filter(statut="S")
  context = {
    'animals': animals
  }
  return HttpResponse(template.render(context))
  
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

""" Model-related routes """

def animal_list(request):
  animals = Animal.objects.filter(statut="S")
  species = Espece.objects.all()
  tags = Tag.objects.all()

  if request.method == 'POST':
    predicates = [('statut', 'S')]
    
    speciesFull = request.POST.get('_especeDropdownFull')
    speciesSmall = request.POST.get('_especeDropdownSmall')
    if speciesSmall:
      predicates.append(('espece_id', speciesSmall))
    
    if speciesFull:
      predicates.append(('espece_id', speciesFull))

    sex = request.POST.get('_sexe')
    if sex:
      predicates.append(('sexe', sex[0]))

    minAge = request.POST.get('_minAge')
    if minAge:
      predicates.append(('age__gte', minAge))

    maxAge = request.POST.get('_maxAge')
    if maxAge:
      predicates.append(('age__lte', maxAge))

    tag = request.POST.getlist('_tag')
    if tag:
      exclusion = []
      for x in tag:
        exclusion.append(('tags__nom__contains', x))

    dpt = request.POST.get('_dptSelect')
    if dpt:
      predicates.append(('refuge__code_postal__startswith', dpt))

    q_list = [Q(x) for x in predicates]
    q_list += [~Q(y) for y in exclusion]

    searchedAnimals = Animal.objects.filter(reduce(operator.and_, q_list)).values()

    template = loader.get_template('animal_list_results.html')
    context = {
      'searchedAnimals': searchedAnimals
    }
    return HttpResponse(template.render(context, request))
  else:
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

def shelters_list(request):
  shelters = Association.objects.all()
  species = Espece.objects.all()
  tags = Tag.objects.all()

  if request.method == 'POST':
    predicates = []

    dptFull = request.POST.get('_dptSelectFull')
    dptSmall = request.POST.get('_dptSelectSmall')
    if dptSmall:
      predicates.append(('code_postal__startswith', dptSmall))
    
    if dptFull:
      predicates.append(('code_postal__startswith', dptFull))

    name = request.POST.get('_shelterNom')

    if name:
      predicates.append(('nom__icontains', name))

    residentSpecies = request.POST.getlist('_espece')

    if residentSpecies:
      predicates.append(('pensionnaires__espece__nom__contains', residentSpecies))

    #! Add check to exclude unavailable animals

    q_list = [Q(x) for x in predicates]

    searchedShelters = Association.objects.filter(reduce(operator.and_, q_list)).values()

    template = loader.get_template('shelters_list_results.html')
    context = {
      'searchedShelters': searchedShelters
    }
    return HttpResponse(template.render(context, request))

  else:
    template = loader.get_template('shelters_list.html')
    context = {
      'associations': shelters,
      'especes': species,
      'tags': tags
    }
    return HttpResponse(template.render(context, request))

def shelters_details(request, shelterId):
  shelter = Association.objects.get(id=shelterId)
  animals = Animal.objects.filter(refuge_id=shelterId)
  template = loader.get_template('shelters_details.html')
  context = {
    'association': shelter,
    'animals': animals
  }
  return HttpResponse(template.render(context, request))

""" Auth-related routes """

def signin_foster(request):
  template = loader.get_template('signin_foster.html')
  return HttpResponse(template.render())

def signin_shelter(request):
  template = loader.get_template('signin_shelter.html')
  return HttpResponse(template.render())

def signin_login(request):
  template = loader.get_template('signin_login.html')
  return HttpResponse(template.render())

""" Foster-related routes
    Hard-coded for now """

def foster_profile(request):
  famille = Famille.objects.get(id=1)
  template = loader.get_template('foster_profile.html')
  context = {
    'famille': famille
  }
  return HttpResponse(template.render(context, request))

def foster_request(request):
  famille = Famille.objects.get(id=1)
  template = loader.get_template('foster_request.html')
  context = {
    'famille': famille
  }
  return HttpResponse(template.render(context,request))

""" Shelter-related routes
    Harde-coded for now """

def shelter_profile(request):
  association = Association.objects.get(id=1)
  template = loader.get_template('shelter_profile.html')
  context = {
    'association': association
  }
  return HttpResponse(template.render(context,request))

def shelter_logo(request):
  association = Association.objects.get(id=1)
  template = loader.get_template('shelter_logo.html')
  context = {
    'association': association
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_list(request):
  association = Association.objects.get(id=1)
  template = loader.get_template('shelter_animal_list.html')
  context = {
    'association': association
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_details(request, animalId):
  association = Association.objects.get(id=1)
  animal = Animal.objects.get(id=animalId)
  template = loader.get_template('shelter_animal_details.html')
  context = {
    'association': association,
    'animal': animal
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_fostered(request):
  association = Association.objects.get(id=1)
  animals = Animal.objects.filter(refuge_id=1, statut="F")
  template = loader.get_template('shelter_animal_fostered.html')
  context = {
    'association': association,
    'animals': animals
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_create(request):
  association = Association.objects.get(id=1)
  species = Espece.objects.all()
  tags = Tag.objects.all()
  template = loader.get_template('shelter_animal_create.html')
  context = {
    'association': association,
    'especes': species,
    'tags': tags,
  }
  return HttpResponse(template.render(context,request))

def shelter_request_list(request):
  association = Association.objects.get(id=1)
  requestedAnimals = Animal.objects.filter(refuge_id=1, statut='S')
  template = loader.get_template('shelter_request_list.html')
  context = {
    'association': association,
    'requestedAnimals': requestedAnimals
  }
  return HttpResponse(template.render(context,request))

def shelter_request_details(request, reqId):
  association = Association.objects.get(id=1)
  req = Demande.objects.get(id=reqId)
  template = loader.get_template('shelter_request_details.html')
  context = {
    'association': association,
    'request': req
  }
  return HttpResponse(template.render(context,request))