from django.shortcuts import render,redirect
from .models import contacts
from django.contrib import messages
from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your views here.
def index(request):
    data=contacts.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        time = models.DateTimeField(auto_now_add=True)
        print(contacts.objects.all())
        query=contacts(name=name,email=email)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        # time = models.DateTimeField(auto_now_add=True)
        time = models.DateTimeField(auto_now_add=True)
        print(contacts.objects.all())

        edit=contacts.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=contacts.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=contacts.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")

def about(request):
    return render(request,"about.html")