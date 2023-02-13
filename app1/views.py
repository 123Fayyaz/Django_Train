from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Train_Details
from app1.forms import train_form
# Create your views here.

def home(Request):
    return render(Request,'app1/train_home.html')

def details(Request):
    form=train_form()
    if Request.method =='post':
        form = train_form(Request.post)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h1>Records updated to trains details</h1>")
    else:
        print("error form invalid")

    return render(Request,'app1/train_details.html',context=dict({'form_d':form}))

def info(Request):
    train_mdl_details=Train_Details.objects.order_by('num')
    train_details_dict={'insert_train_details':train_mdl_details}
    return render(Request,'app1/train_info.html',context=train_details_dict)










