from django.shortcuts import render
from app.forms import *

# Create your views here.
def root(request):
    form = HeyForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        sent = (f"Hey, {name}!")
        return render(request, "root.html", {"name": name, "sent": sent, "form": form})
    else:
        return render(request, "root.html", {"form": form})
    
def age(request):
    form = Age(request.GET)
    if form.is_valid():
        x = form.cleaned_data["x"]
        y = form.cleaned_data["y"]
        answer = x - y
        return render(request, "root.html", {"x": x, "y": y, "answer": answer, "form": form})
    else:
        return render(request, "root.html", {"form": form})

def badburger(request):
    form = BadBurger(request.GET)
    if form.is_valid():
        drinks = form.cleaned_data["drinks"]
        burger = form.cleaned_data["burger"]
        fries = form.cleaned_data['fries']
        total = (drinks * 1) + (burger * 4.5) + (fries * 1.5)
        return render(request, "root.html", {"burger": burger, "fries": fries, "drinks": drinks, "total": total, "form": form})
    else:
        return render(request, 'root.html', {"form": form})