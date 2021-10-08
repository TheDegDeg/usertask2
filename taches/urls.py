from django.urls import path
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index , name='home page'),
    path('modifier/<str:pk>/',views.modifier , name='modifier'),
   path('supprimer/<str:pk>/',views.supprimer , name='supprimer'),
]