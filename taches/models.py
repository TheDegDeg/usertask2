from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Tache(models.Model):
    titre = models.CharField(max_length=100)
   
    date = models.DateField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.titre



# Create your models here.
