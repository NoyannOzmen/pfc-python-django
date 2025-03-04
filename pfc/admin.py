from django.contrib import admin
from .models import *

# Register your models here.

class UtilisateurAdmin(admin.ModelAdmin):
  list_display = ("id", "email", "accueillant", "refuge")

class FamilleAdmin(admin.ModelAdmin):
  list_display = ( "prenom", "nom")

class EspeceAdmin(admin.ModelAdmin):
  list_display = ("id", "nom")

class TagAdmin(admin.ModelAdmin):
  list_display = ("id" ,"nom", "description")

class MediaAdmin(admin.ModelAdmin):
  list_display = ("id", "url")

class AssociationAdmin(admin.ModelAdmin):
  list_display = ( "nom", "code_postal")

class AnimalAdmin(admin.ModelAdmin):
  list_display = ("id", "nom", "age", "sexe")

class DemandeAdmin(admin.ModelAdmin):
  list_display = ("id", "date_debut", "date_fin")

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Famille, FamilleAdmin)
admin.site.register(Espece, EspeceAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Association, AssociationAdmin)
admin.site.register(Animal, AnimalAdmin) 
admin.site.register(Demande, DemandeAdmin)