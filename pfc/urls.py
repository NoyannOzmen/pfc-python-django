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
    path('connexion', views.signin_login, name='login'),
    path('animaux/', views.animal_list, name='animal_list'),
    path('animaux/<int:animalId>', views.animal_details, name='animal_details'),
    path('associations/', views.shelter_list, name='shelter_list'),
    path('associations/<int:shelterId>', views.shelter_details, name='shelter_details'),
    path("__reload__/", include("django_browser_reload.urls")),
]