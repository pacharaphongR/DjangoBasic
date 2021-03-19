from django.shortcuts import render,redirect
# from django.http import HttpResponse

# # Create your views here.
# def hello(request):
#     return HttpResponse("<h2>hello world</h2>")

# def hello(request):
#     tags=['น้ำตก','ธรรมชาติ','หมอก']
#     # rating = 3
#     rating = 4
#     return render(request,'index.html',
#     {
#         'name':'บทความท่องเที่ยวภาคเหนือ',
#         'author':'Pacharaphong',
#         'tags':tags,
#         'rating':rating
#         })
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages

def hello(request):
    #query from model
    data = Post.objects.all()
    return render(request,'index.html',{'posts':data})
def page1(request):
    return render(request,'page1.html')
def createForm(request):
    return render(request,'form.html')
def addBlog(request):
    name = request.POST['name']
    description = request.POST['description']
    return render(request,'result.html',{'name':name,'description':description})
def registerForm(request):
    return render(request,'form-register.html')
def createUser(request):
    #register
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username has already exist')
            return redirect('/registerForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email has already exist')
            return redirect('/registerForm')
        else:
            user = User.objects.create_user(
            username=username,
            password = password,
            email = email,
            first_name = firstname,
            last_name = lastname
            )
            user.save()
            return redirect('/')
    else:
        messages.info(request,'Password is not match')
        return redirect('/registerForm')

def loginForm(request):
    return render(request,'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    #login
    user = auth.authenticate(username=username,password=password)

    #check username password
    if user is not None :
        auth.login(request,user)
        return redirect('/')
    else: 
        messages.info(request,'User not found')
        return redirect('/loginForm')
def logout(request):
    auth.logout(request)
    return redirect('/')
