from django.shortcuts import render, redirect

##let's import user model to create user for our app
from django.contrib.auth.models import User,auth
from django.contrib import messages

from .models import Profile

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method=="POST":
        #let's get all the values passed using post method
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            #check whether email is already taken by user or not
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists(): #check whether username is already taken
                messages.info(request,'Username Taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #log user in and redirect to settings page

                #create a profile object for the newuser
                user_model = User.objects.get(username=username)
                new_profile= Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request,'Password Not Matching')
            return redirect('signup')


    else:
        return render(request,'signup.html')