from django.shortcuts import render

from vtart.models import VaultTrain

# Create your views here.
def index (request) :
    all = VaultTrain.objects.all()
    needed = []

    for i in range(5):
        needed.append(all[i])

    return render(request , "index.html",{
        "line" : needed,
    })

def detail (request):
    return render(request, "detail.html", {})

def userform (request):
    return render(request, "userform.html",{})

def map(request):
    return render(request,"map.html",{})
