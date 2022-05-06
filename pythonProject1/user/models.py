from django.db import models
from conference.models import Conference

# Create your models here.
class User(models.Model):
    conference=models.ForeignKey(Conference,null=True,on_delete=models.SET_NULL)

    nom=models.CharField(max_length=200,null=True)
    prenom=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    telephone=models.IntegerField(null=True)


    def __str__(self):
        return self.nom
