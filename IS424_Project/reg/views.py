from django.http import HttpResponse
from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Course,College,Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
import time


# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["UserName"]
        password = request.POST["passWord"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return HttpResponseRedirect(reverse("index"))
            return HttpResponseRedirect("/reg/")
        else:
            user = User.objects.filter(username=username).first()
            if user is not None:
                return render(request, "reg/login.html", {"message": "Incorrect password."})  
            else:
                return render(request, "reg/login.html", {"message": "Username doesn't exist."})  
    else:
        return render(request, "reg/login.html")

def index(request):
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login_view")) 
         return HttpResponseRedirect("/reg/login") 
    sid=request.user.username
    u=User.objects.get(username=sid)
    student = Student.objects.get(user=u)
    message='Here is a list of courses to Register in'
    unreg = Course.objects.exclude(students=student).all()
    return render(request,'reg/index.html',{"courses":unreg ,'message':message })#,'student':student

def display (request,cid):#sid
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login_view")) 
         return HttpResponseRedirect("/reg/login") 
    #sid=request.user.username
    course = Course.objects.get(courseid=cid)
    #u=User.objects.get(username=sid)
    #student = Student.objects.get(user=u)
    return render(request, r"reg/display.html", {"COU": course })#"STU": student

def add(request,cid):#sid
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login_view")) 
         return HttpResponseRedirect("/reg/login") 
    if request.method == "POST":
        sid=request.user.username
        course = Course.objects.get(courseid = cid)
        u=User.objects.get(username=sid)
        student = Student.objects.get(user=u)
        student.courses.add(course)
        return HttpResponseRedirect("/reg/")
        #return HttpResponseRedirect(reverse("index")) 
    return HttpResponseRedirect("/reg/")
    


def update(request):#sid
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login_view")) 
         return HttpResponseRedirect("/reg/login") 
    sid=request.user.username
    u=User.objects.get(username=sid)
    student = Student.objects.get(user=u)
    message = "Here is a list of courses you are registered in "
    regcourses = student.courses.all()
    return render(request,"reg/update.html",{"courses":regcourses ,'message':message , "student":student})

def remove(request, cid): #sid
    if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login_view")) 
         return HttpResponseRedirect("/reg/login") 
    sid=request.user.username
    course = Course.objects.get(courseid = cid)
    u=User.objects.get(username=sid)
    student = Student.objects.get(user=u)
    student.courses.remove(course)
    #return HttpResponseRedirect(f"/reg/")
    #return HttpResponseRedirect(reverse("index")) 
    return HttpResponseRedirect(f"/reg/update")





def signup(request):
    if request.method == "POST":
        un = request.POST["UserName"]
        pw = request.POST["passWord"]
        fname = request.POST["firstName"]
        lname = request.POST["lastName"]
        
        # Validate non-empty inputs
        if not all([un, pw, fname, lname]):
            return render(request, "reg/signup.html", {"message": "All fields are required"})  
        # Validate username
        username_validator = UnicodeUsernameValidator()
        try:
            username_validator(un)
        except ValidationError:
            return render(request, "reg/signup.html", {"message": "All fields are required"})  
        
        if User.objects.filter(username=un).exists():
                return render(request, "reg/signup.html", {"message": "Username already exists"})
       
        # Validate password
        if len(pw) < 6:
            return render(request, "reg/signup.html", {"message": "Password must be at least 6 characters long"})  

        # Validate first and last names
        if any(char.isdigit() for char in fname) or any(char.isdigit() for char in lname):
            return render(request, "reg/signup.html", {"message": "First name and last name cannot contain numbers"})  
        

        u = User.objects.create_user(username=un, password=pw, first_name=fname, last_name=lname)
        s = Student(user=u)
        s.save()
        return render(request, "reg/login.html")
    
    return render(request, "reg/signup.html")
    
   
def logout_view(request):
    logout(request)
    return render(request, "reg/login.html")



