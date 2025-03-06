from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import *
from django.db.models import Q
import operator
from functools import reduce
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib import messages
import bcrypt 
  
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

# Model-related routes

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

  if request.method == 'POST':
    foster_id = request.session["foster_id"]
    famille = Famille.objects.get(id=foster_id)
    start_date = date.today()
    end_date = start_date + relativedelta(years=1)

    try:
      requested = Demande.objects.get(famille=famille, animal=animal)
      context['error'] = 'Vous avez déjà effectué une demande pour cette animal'
    except :
      newRequest = Demande(famille=famille, animal=animal, date_debut=start_date, date_fin=end_date)
      newRequest.save()
      context['message'] = 'Votre demande a bien été prise en compte !'
    
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

  if request.method == 'POST':
    last_name = request.POST.get('_nom')
    first_name = request.POST.get('_prenom')
    telephone = request.POST.get('_telephone')
    hebergement = request.POST.get('_hebergement')
    terrain = request.POST.get('_terrain')
    rue = request.POST.get('_rue')
    commune = request.POST.get('_commune')
    code_postal = request.POST.get('_code_postal')
    pays = request.POST.get('_pays')
    email = request.POST.get('_email')
    password = request.POST.get('_password')
    confirmation = request.POST.get('_confirmation')

    user = Utilisateur.objects.filter(email=email)

    if user.exists():
      messages.info(request, "Invalid credentials")
      return HttpResponse(template.render())
    
    if not password == confirmation:
      messages.info(request, "Please make sure your password is correct in both fields")
      return HttpResponse(template.render())
    
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    string_password = hash.decode('utf8')

    user = Utilisateur(email=email, password=string_password)
    user.save()

    foster = Famille(
      prenom=first_name,
      nom=last_name,
      telephone=telephone,
      hebergement=hebergement,
      rue=rue,
      commune=commune,
      code_postal=code_postal,
      pays=pays
    )

    if terrain:
      foster.terrain = terrain

    foster.save()
    user.accueillant=foster
    user.save()

    messages.info(request, "Account created Successfully!")
    return redirect('/')
  
  context = {}
  return HttpResponse(template.render(context, request))

def signin_shelter(request):
  template = loader.get_template('signin_shelter.html')

  if request.method == 'POST':
    name = request.POST.get('_nom')
    responsable = request.POST.get('_responsable')
    rue = request.POST.get('_rue')
    commune = request.POST.get('_commune')
    code_postal = request.POST.get('_code_postal')
    pays = request.POST.get('_pays')
    telephone = request.POST.get('_telephone')
    siret = request.POST.get('_siret')
    site = request.POST.get('_site')
    description = request.POST.get('_description')
    email = request.POST.get('_email')
    password = request.POST.get('_password')
    confirmation = request.POST.get('_confirmation')

    user = Utilisateur.objects.filter(email=email)

    if user.exists():
      messages.info(request, "Invalid credentials")
      return HttpResponse(template.render())
    
    if not password == confirmation:
      messages.info(request, "Please make sure your password is correct in both fields")
      return HttpResponse(template.render())
    
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    string_password = hash.decode('utf8')
    
    user = Utilisateur.ojects.create_user(email=email, password=string_password)
    user.save()

    shelter = Association(
      nom=name,
      responsable=responsable,
      telephone=telephone,
      rue=rue,
      commune=commune,
      code_postal=code_postal,
      pays=pays,
      siret=siret
    )

    if site:
      shelter.site = site

    if description:
      shelter.description = description

    shelter.save()
    user.refuge = shelter
    user.save()

    messages.info(request, "Account created Successfully!")
    return redirect('/') 

  context = {}
  return HttpResponse(template.render(context, request))

def signin_login(request):
  template = loader.get_template('signin_login.html')

  if request.method == "POST":
    email = request.POST.get('_email')
    userPassword = request.POST.get('_password')

    if not Utilisateur.objects.filter(email=email).exists():
      messages.error(request, 'Invalid credentials')
      return HttpResponse(template.render()) 
   
    user = Utilisateur.objects.get(email=email)
    hash = user.password.encode('utf-8')
    bytes = userPassword.encode('utf-8')
    result = bcrypt.checkpw(bytes, hash)
    print(result)

    if user is None or result is False:
      messages.error(request, 'Invalid credentials')
      return render(request, 'signin_login.html')
    else:
      request.session["isLoggedIn"] = True
      request.session["user_id"] = user.id
      if user.accueillant:
        request.session["foster_id"] = user.accueillant.id
      if user.refuge:
        request.session["shelter_id"] = user.refuge.id
      return HttpResponse(template.render({'user' : user }, request))

  context = {}
  return HttpResponse(template.render(context, request))

def signin_logout(request):
  user = None
  request.session = None
  return redirect("main")

# Foster-related routes

def foster_profile(request):
  foster_id = request.session["foster_id"]
  famille = Famille.objects.get(id=foster_id)
  template = loader.get_template('foster_profile.html')
  context = {
    'famille': famille
  }

  if request.method == 'POST':
    delete_account = request.POST.get("delete_account")
    edit_infos = request.POST.get("edit_infos")

    if edit_infos :
      last_name = request.POST.get('_nom')
      first_name = request.POST.get('_prenom')
      hebergement = request.POST.get('_hebergement')
      terrain = request.POST.get('_terrain')
      rue = request.POST.get('_rue')
      commune = request.POST.get('_commune')
      code_postal = request.POST.get('_code_postal')

      if last_name:
        famille.nom = last_name
      if first_name:
        famille.prenom = first_name
      if hebergement:
        famille.hebergement = hebergement
      if terrain:
        famille.terrain = terrain
      if rue:
        famille.rue = rue
      if commune:
        famille.commune = commune
      if code_postal:
        famille.code_postal = code_postal

      famille.save()
    if delete_account:
      user_id = request.session['user_id']
      user = Utilisateur.objects.get(id=user_id)

      user.delete()
      famille.delete()

      messages.error(request, 'Sad to see you go')
      return render(request, 'main.html')

  return HttpResponse(template.render(context, request))

def foster_request(request):
  foster_id = request.session["foster_id"]
  famille = Famille.objects.get(id=foster_id)
  template = loader.get_template('foster_request.html')
  context = {
    'famille': famille
  }
  return HttpResponse(template.render(context,request))

# Shelter-related routes

def shelter_profile(request):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  template = loader.get_template('shelter_profile.html')
  context = {
    'association': association
  }

  if request.method == 'POST':
    delete_account = request.POST.get("delete_account")
    edit_infos = request.POST.get("edit_infos")

    if edit_infos :
      name = request.POST.get('_nom')
      owner = request.POST.get('_president')
      rue = request.POST.get('_rue')
      commune = request.POST.get('_commune')
      code_postal = request.POST.get('_code_postal')
      pays = request.POST.get('_pays')
      telephone = request.POST.get('_telephone')
      siret = request.POST.get('_siret')
      site = request.POST.get('_site')
      description = request.POST.get('_description')

      if name:
        association.nom = name
      if owner:
        association.responsable = owner
      if rue:
        association.rue = rue
      if commune:
        association.commune = commune
      if code_postal:
        association.code_postal = code_postal
      if pays:
        association.pays = pays
      if telephone:
        association.telephone = telephone
      if siret:
        association.siret = siret
      if site:
        association.site = site
      if description:
        association.description = description

      association.save()
    
    if delete_account:
      user_id = request.session['user_id']
      user = Utilisateur.objects.get(id=user_id)

      user.delete()
      association.delete()

      messages.error(request, 'Sad to see you go')
      return render(request, 'main.html')

  return HttpResponse(template.render(context,request))

def shelter_logo(request):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  template = loader.get_template('shelter_logo.html')
  context = {
    'association': association
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_list(request):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  template = loader.get_template('shelter_animal_list.html')
  context = {
    'association': association
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_details(request, animalId):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  animal = Animal.objects.get(id=animalId)
  template = loader.get_template('shelter_animal_details.html')
  context = {
    'association': association,
    'animal': animal
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_fostered(request):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  animals = Animal.objects.filter(refuge_id=1, statut="F")
  template = loader.get_template('shelter_animal_fostered.html')
  context = {
    'association': association,
    'animals': animals
  }
  return HttpResponse(template.render(context,request))

def shelter_animal_create(request):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  species = Espece.objects.all()
  tags = Tag.objects.all()
  template = loader.get_template('shelter_animal_create.html')
  context = {
    'association': association,
    'especes': species,
    'tags': tags,
  }

  if request.method == 'POST':
    animalForm = request.POST.get('create_animal')
    tagForm = request.POST.get('create_tag')

    if animalForm:
      name = request.POST.get('_nom_animal')
      sex = request.POST.get('_sexe_animal')
      age = request.POST.get('_age_animal')
      animalSpecies = request.POST.get('_espece_animal')
      espece = Espece.objects.get(id=animalSpecies)
      race = request.POST.get('_race_animal')
      colour = request.POST.get('_couleur_animal')
      description = request.POST.get('_description_animal')
      animalTags = request.POST.getlist('_tag')

      newAnimal = Animal(nom=name, sexe=sex[0], espece=espece, age=age, couleur=colour, description=description, refuge=association)
      newAnimal.save()

      if race :
        newAnimal.race = race
      if animalTags:
        newAnimal.tags.set(animalTags)

      newAnimal.save()

    if tagForm:
      tag_name = request.POST.get('_name_tag')
      tag_desc = request.POST.get('_desc_tag')

      newTag = Tag(nom = tag_name, description = tag_desc)
      newTag.save()

  return HttpResponse(template.render(context,request))

def shelter_request_list(request):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  requestedAnimals = Animal.objects.filter(refuge_id=shelter_id, statut='S')
  template = loader.get_template('shelter_request_list.html')
  context = {
    'association': association,
    'requestedAnimals': requestedAnimals
  }
  return HttpResponse(template.render(context,request))

def shelter_request_details(request, reqId):
  shelter_id = request.session["shelter_id"]
  association = Association.objects.get(id=shelter_id)
  req = Demande.objects.get(id=reqId)
  template = loader.get_template('shelter_request_details.html')
  context = {
    'association': association,
    'request': req
  }

  if request.method == 'POST':
    accept_request = request.POST.get('accept_request')
    deny_request = request.POST.get('deny_request')

    if accept_request:
      req.statut_demande = "Acc"
      req.save()
    if deny_request:
      req.statut_demande = "Den"
      req.save()

  return HttpResponse(template.render(context,request))