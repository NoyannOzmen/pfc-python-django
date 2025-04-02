from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

class Famille(models.Model):
  prenom = models.CharField(max_length=255, blank=True, null=True)
  nom = models.CharField(max_length=255)
  rue = models.CharField(max_length=255)
  commune = models.CharField(max_length=255)
  code_postal = models.CharField(max_length=255)
  pays = models.CharField(max_length=255)
  telephone = models.CharField(max_length=255)
  hebergement = models.CharField(max_length=255)
  terrain = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return f"{self.nom}"
  
class Espece(models.Model):
  nom = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.nom}"

class Tag(models.Model):
  nom = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.nom}"
  
class Association(models.Model):
  nom = models.CharField(max_length=255)
  responsable = models.CharField(max_length=255)
  rue = models.CharField(max_length=255)
  commune = models.CharField(max_length=255)
  code_postal = models.CharField(max_length=255)
  pays = models.CharField(max_length=255)
  siret = models.CharField(max_length=255)
  telephone = models.CharField(max_length=255)
  site = models.CharField(max_length=255, blank=True, null=True)
  description = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return f"{self.nom}"

class Animal(models.Model):
  class Sexe(models.TextChoices):
    MALE = "M", _("Mâle")
    FEMALE = "F", _("Femelle")
    UNKNOWN = "U", _("Inconnu")
  
  class Statut(models.TextChoices):
    SHELTERED = "S", _("En refuge")
    FOSTERED = "F", _("Accueilli")
    ADOPTED = "A", _("Adopté")

  nom = models.CharField(max_length=255)
  race = models.CharField(max_length=255, blank=True, null=True)
  couleur = models.CharField(max_length=255)
  age = models.IntegerField()
  sexe = models.CharField(
      max_length=2,
      choices=Sexe.choices,
      default=Sexe.UNKNOWN,
  )
  description = models.CharField(max_length=255, blank=True, null=True)
  statut = models.CharField(
      max_length=2,
      choices=Statut.choices,
      default=Statut.SHELTERED,
  )
  espece = models.ForeignKey(Espece, on_delete=models.CASCADE)
  refuge = models.ForeignKey(Association, related_name='pensionnaires', on_delete=models.CASCADE)
  accueillant = models.ForeignKey(Famille, blank=True, null=True, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, blank=True)

  potentiel_accueillant = models.ManyToManyField(Famille, related_name='potentiel_accueillant', through='Demande')

  def __str__(self):
    return f"{self.nom}"
  
class Media(models.Model):
  url = models.ImageField(upload_to='images/animaux', null=True)
  ordre = models.IntegerField()
  animal = models.ForeignKey(Animal, related_name='images_animal', blank=True, null=True, on_delete=models.CASCADE)
  association = models.ForeignKey(Association, related_name='images_association', blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.url}"

class Demande(models.Model):
  class Statut_Demande(models.TextChoices):
    PENDING = "Pen", _("En attente")
    ACCEPTED = "Acc", _("Validée")
    DENIED = "Den", _("Refusée")
  
  famille = models.ForeignKey(Famille, related_name="demandes", on_delete=models.CASCADE)
  animal = models.ForeignKey(Animal, related_name="demandes", on_delete=models.CASCADE)
  statut_demande = models.CharField(
      max_length=3,
      choices=Statut_Demande.choices,
      default=Statut_Demande.PENDING,
  )
  date_debut = models.DateField()
  date_fin = models.DateField()
  def __str__(self):
    return f"{self.famille.nom} {self.date_debut}"
  
class Utilisateur(AbstractBaseUser):

  email = models.EmailField(unique=True)
  password = models.CharField(max_length=255, unique=True)
  refuge  = models.ForeignKey(
        Association,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='identifiant_association'
  )
  accueillant  = models.ForeignKey(
      Famille,
      blank=True,
      null=True,
      on_delete=models.CASCADE,
      related_name='identifiant_famille'
  )
  last_login = None
  USERNAME_FIELD = 'email'

  def __str__(self):
    return f"{self.email}"
  
  class Meta:
        db_table='pfc_utilisateur'