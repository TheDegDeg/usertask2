from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class UserForm(forms.Form):
    class Meta : 
        models = Utilisateur
        fields = '__all__'

class TacheForm(forms.ModelForm):
    class Meta : 
        model = Tache
        fields = ('titre',)



# creer un formulaire basé sur notre model avec tout les champs pour les mettre dans le formulaire