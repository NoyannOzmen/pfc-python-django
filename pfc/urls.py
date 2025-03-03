from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("__reload__/", include("django_browser_reload.urls")),
]