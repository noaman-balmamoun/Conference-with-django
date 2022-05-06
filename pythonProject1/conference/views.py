from django.shortcuts import render
from conference.models import Conference
from user.models import User


def home(request):

    conferences=Conference.objects.all()
    users = User.objects.all()
    context={'conferences':conferences,'users':users}
    return render(request,'conference/acceuil.html',context)

# Create your views here.
