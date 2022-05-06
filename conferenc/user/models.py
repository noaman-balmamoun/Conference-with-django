from django.db import models

# Create your models here.
class User(models.Model):
    nom=models.CharField(max_length=200, null=True)
    Prenom=models.CharField(max_length=200,null=True)
    date_creation=models.DateTimeField(auto_now_add=True, null=True)
    telephone=models.FloatField(max_length=200,null=True)



    def __str__(self):
        return self.nom
