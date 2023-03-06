from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *

def index(request):
    if request.method == "POST":
				# create a new copy of the form with the data the user 
				# entered , it is stored in request.POST
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            request.session["pizza_id"] = pizza.id
            return redirect('details')
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'index.html', {'form': form})
    else:
        # normal get request, user wants to see the form 
        form = PizzaForm()
        return render(request, 'index.html', {'form': form})

def details(request):
    if request.method == "POST":
				# create a new copy of the form with the data the user 
				# entered , it is stored in request.POST
        form = CustomerForm(request.POST)
        if form.is_valid():
            order = form.save()
            request.session["order_name"] = order.name
            return redirect('created')
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'details.html', {'form': form})
    else:
        # normal get request, user wants to see the form 
        form = CustomerForm()
        return render(request, 'details.html', {'form': form})

def created(request):
    pizza = get_object_or_404(Pizza, id = request.session.get("pizza_id"))
    name = request.session.get("order_name")
    return render(request, 'created.html', {"pizza":pizza, "name": name})