from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def users(request):
    return render(request,'users/user.html ')




# Create your views here.
