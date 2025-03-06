from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('a-propos/', views.static_about, name='about'),
    path('devenir-famille-d-accueil/', views.static_become_foster, name='become_foster'),
    path('contact/', views.static_contact, name='contact'),
    path('faq/', views.static_faq, name='faq'),
    path('rgpd/', views.static_gdpr, name='gdpr'),
    path('infos-legales/', views.static_legal, name='legal'),
    path('plan/', views.static_map, name='map'),
    path('famille/inscription', views.signin_foster, name='foster_signup'),
    path('association/inscription/', views.signin_shelter, name='shelter_signup'),
    path('connexion/', views.signin_login, name='login'),
    path('deconnexion/', views.signin_logout, name='logout'),
    path('animaux/', views.animal_list, name='animal_list'),
    path('animaux/<int:animalId>', views.animal_details, name='animal_details'),
    path('associations/', views.shelters_list, name='shelters_list'),
    path('associations/<int:shelterId>', views.shelters_details, name='shelters_details'),
    path("famille/profil", views.foster_profile, name='foster_profile'),
    path("famille/profil/demandes", views.foster_request, name='foster_request'),
    path("association/profil", views.shelter_profile, name='shelter_profile'),
    path("association/profil/logo", views.shelter_logo, name='shelter_logo'),
    path("association/profil/animaux", views.shelter_animal_list, name='shelter_animal_list'),
    path("association/profil/animaux/<int:animalId>", views.shelter_animal_details, name='shelter_animal_details'),
    path("association/profil/animaux/suivi", views.shelter_animal_fostered, name='shelter_animal_fostered'),
    path("association/profil/animaux/nouveau-profil", views.shelter_animal_create, name='shelter_animal_create'),
    path("association/profil/demandes", views.shelter_request_list, name='shelter_request_list'),
    path("association/profil/demandes/<int:reqId>", views.shelter_request_details, name='shelter_request_details'),
    path("__reload__/", include("django_browser_reload.urls")),
]