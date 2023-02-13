from django.contrib import admin
from django.urls import path, re_path,include
from app1 import views as v

urlpatterns = [

    re_path(r'^train_home', v.home),
    re_path(r'^train_details', v.details),
    re_path(r'^train_info',v.info),


]