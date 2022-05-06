from django.db import models

# Create your models here.
class Conference(models.Model):

    nom=models.CharField(max_length=200,null=True)
    lieu=models.CharField(max_length=200,null=True)
    date=models.DateField(null=True)
    categorie=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=400,null=True)


    def __str__(self):
        return self.nom
