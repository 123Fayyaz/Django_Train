from django.shortcuts import render
from django.http import HttpResponse
from train_fare.models import fare
from train_fare.forms import enter_fare
# Create your views here.

def fare(Request):
    form=enter_fare()
    if Request.method =='post':
        form = enter_fare(Request.post)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Records inserted successfully</h1>")
    else:
        print("error form invalid")
    return render(Request,'trani_fare/fare.html',{'form':form})