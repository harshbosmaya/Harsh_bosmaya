from django.shortcuts import render,redirect
from .models import contacts
from django.contrib import messages
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Max
from django.db.models import F
from django.db.models import Q

# Create your views here.
def index(request):
    data=contacts.objects.all()
    print(data)
    context={"data":data}
    # data = {'name':data[0].name,'email':data[0].email,'time':data[0].time}
    # context={"data":}
    return render(request,"index.html",context)

def create(request):
    data=contacts.objects.all()
    print(data)
    context={"data":data}
    return render(request,"create.html",{"form":data})#created new def for create page

def insertData(request):                         #temporary comment for testing create page
    count= contacts.objects.all().count()
    if request.method=="POST" and count == 0:
        initial_id = 1
        name=request.POST.get('name')
        email=request.POST.get('email')
        notes=request.POST.get('notes')
        time = models.DateTimeField(auto_now_add=True)
        print(contacts.objects.all())
        query=contacts(id=initial_id,name=name,email=email,notes=notes)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    if request.method=="POST" and count > 0:
        max_id = contacts.objects.aggregate(Max('id'))['id__max'] or 0
        next_id = max_id + 1
        name=request.POST.get('name')
        email=request.POST.get('email')
        notes=request.POST.get('notes')
        time = models.DateTimeField(auto_now_add=True)
        if contacts.objects.filter(Q(name=name) | Q(email=email)).exists():
            messages.info(request, "Email and/or Name already exists in records.")
        else:
            print(contacts.objects.all())
            query=contacts(id=next_id,name=name,email=email,notes=notes)
            query.save()
            messages.info(request,"Data Inserted Successfully")
        return redirect("/")

    return render(request,"index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        notes=request.POST['notes']
        # time = models.DateTimeField(auto_now_add=True)
        time = models.DateTimeField(auto_now_add=True)
        print(contacts.objects.all())
        if contacts.objects.filter(Q(name=name) | Q(email=email)).exclude(id=id).exists():
            messages.info(request, "Email and/or Name already exists in records.")
        else:
            edit=contacts.objects.get(id=id)
            edit.name=name
            edit.email=email
            edit.notes=notes
            edit.save()
            messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=contacts.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)



# # new code
# def deleteData(request, id):
#     contact = contacts.objects.get(id=id)
#     return redirect("/")  # Redirect to index if the contact doesn't exist

#     context = {"contact": contact}
#     return render(request, "confirm_delete.html", context)

# def confirm_function(request, id):
#     d = contacts.objects.get(id=id)
#     d.delete()
#     messages.error(request, "Data deleted Successfully")
#     contacts.objects.filter(id__gt=id).update(id=F('id') - 1)
#     return redirect("/")




def deleteData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        notes=request.POST['notes']
        time = models.DateTimeField(auto_now_add=True)
        print(contacts.objects.all())

    d=contacts.objects.get(id=id) 
    context={"d":d}
    print(d.notes)
    return render(request,"confirm_delete.html",context)
# old code
# def deleteData(request,id):
#     context = {"id":id}
#     return render(request,"confirm_delete.html",context)

def confirm_function(request,id):
    d=contacts.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    contacts.objects.filter(id__gt=id).update(id=F('id') - 1)
    return redirect("/")

def about(request):
    return render(request,"about.html")