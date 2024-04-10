from django.shortcuts import render, redirect
from.forms import UserFormInput
from vtart.models import VaultTrain
from random import randint

# Create your views here.
def index(request) :
    all = VaultTrain.objects.all()
    needed = []

    for i in range(5):
        needed.append(all[i])

    lucky = randint(0,4) # J'ai mis 5 parce que j'ai pas toutes les images

    return render(request , "index.html",{
        "line" : needed,
        "lucky" : all[lucky]
    })

def detail (request, name):
    train = VaultTrain.objects.get(name = name)
    
    return render(request, "detail.html", {'train': train})

def userform (request):
    if request.method == 'POST':
        form = UserFormInput(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/vtart/')
    else:
        form = UserFormInput()
    return render(request, 'userform.html', {'form': form})


def map(request):
    return render(request,"map.html",{})
