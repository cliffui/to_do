from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    if request.method=="POST":
        if request.user is not None:
          list_name=request.POST['list_name'] 

          list=List(body=list_name)
          list.user=request.user
          list.save()
          return redirect('/')
        else:
            messages.info(request,"Your To Do List Is Empty")
            return redirect('/')
    else:
        return render(request,"dashboard.html",)
def edit(request,list_id):
    list=List.objects.get(id=list_id)
    return render(request,"edit.html",{"list":list})

def edit_record(request,list_id):
    if request.method=="POST":
        list_name=request.POST['list_name']

        list=List.objects.get(id=list_id)
        list.body=list_name
        list.save()
        messages.info(request,"Your List Was Edited Successfully")
        return redirect('/')
def delete(request,list_id):
    list=List.objects.get(id=list_id)
    list.delete()
    return redirect("/")

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Taken")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Used")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                new_model=User.objects.get(username=username)
                create_profile=Profile.objects.create(user=new_model)
                create_profile.save()
                return render(request,'success.html',{"new_model":new_model})
        else:
            messages.info(request,"Password Not The Same")
            return redirect("register")
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Credentials Invalid")
            return redirect("login")
    else:
        return render(request,"login.html")