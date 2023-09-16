#------------CREATE REGISTRATION PAGE---------
from django.shortcuts import render,redirect
from django .http import HttpResponse
from . models import india
from . forms import indiaform

def create(request):
    if request.method=="POST":
        form=indiaform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('read')
    else:
        form=indiaform()
        return render(request,'create.html',{'form':form})    
    
#-----------READ PAGE-----------------

def read(request):
    obj=india.objects.all()
    return render(request,'read.html',{'obj':obj})

#-----------DELETE PAGE--------------

def delete(request,id):
    obj=india.objects.get(id=id)
    obj.delete()
    return redirect('read')

#-------------EDIT PAGE----------------

def edit(request,id):
    data=india.objects.get(id=id)
    if request.method=='POST':
        fm=indiaform(request.POST,instance=data)
        if fm.is_valid:
            fm.save()
            return redirect('read')
    else:
        data1=indiaform(instance=data)
        return render(request,'edit.html',{'data1':data1})    