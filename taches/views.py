from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .models import *
from .forms import * 

def index(request):

    usr = Utilisateur.objects.all()
    form2 = UserForm()
    form1 = TacheForm()
    taches = Tache.objects.all()
   

    if request.method =='POST':
        form1 = TacheForm(request.POST)
        form2 = UserForm(request.POST)
        if form1.is_valid() and form2.is_valid:
            form1.save()
            #form2.save()
        return redirect('/')

    return render(request,'taches/list.html' , context={'taches' : taches,'form1':form1 , 'form2' : form2})

def modifier(request, pk):
    #user = Utilisateur.objects.get(id = pk)
    tache = Tache.objects.get(id = pk)

    form1 = TacheForm(instance=tache)
    if request.method =='POST':
        form1 = TacheForm(request.POST, instance=tache)
        #form2 = UserForm(request.POST, instance=user)
        if form1.is_valid():
            form1.save()
           # form2.save()
            return redirect('/')

    return render(request , 'taches/modifier.html', context={'form':form1 },)

def supprimer(request, pk) : 
        suppr = Tache.objects.get(id = pk)

        if request.method =='POST' : 
            suppr.delete()
            return redirect('/')
        #return render(request , 'taches/supprimer.html')
        return render(request , 'taches/supprimer.html',context={'suppr': suppr})



# Create your views here.
