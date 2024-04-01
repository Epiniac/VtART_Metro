from django.shortcuts import render
from vtart.models import VaultTrain

# Create your views here.
def index (request) :
    lines = VaultTrain.objects.all()
    return render(request , "index.html",{})

def detail (request):
    return render(request, "detail.html", {})

def userform (request):
    return render(request, "userform.html",{})
