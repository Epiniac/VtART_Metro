from django.shortcuts import render

from vtart.models import VaultTrain

# Create your views here.
def index (request) :
    mytrain = VaultTrain.objects.all()[:5]  # 5 first train, available

    lines = VaultTrain.objects.all()
    return render(request , "index.html",{
        "name" : mytrain.name,
        "destination" : mytrain.destination,
        "logo" : mytrain.logo,
        "time" : mytrain.time
    })

def detail (request):
    return render(request, "detail.html", {})

def userform (request):
    return render(request, "userform.html",{})
