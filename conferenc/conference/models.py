from django.db import models

# Create your models here.
class Conference(models.Model):
    nom=models.CharField(max_length=200, null=True)
    type=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True, null=True)
    nombre_place=models.FloatField(max_length=200,null=True)
    local=models.CharField(max_length=200,null=True)



    def __str__(self):
        return self.nom